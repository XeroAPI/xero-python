# xero-python
[![PyPI version](https://badge.fury.io/py/xero-python.svg)](https://badge.fury.io/py/xero-python)
[![Github forks](https://img.shields.io/github/forks/XeroAPI/xero-python.svg)](https://github.com/XeroAPI/xero-python/network)
[![Github stars](https://img.shields.io/github/stars/XeroAPI/xero-python.svg)](https://github.com/XeroAPI/xero-python/stargazers)
[![Downloads](https://pepy.tech/badge/xero-python)](https://pepy.tech/project/xero-python)

The xero-python SDK makes it easy for developers to access Xero's APIs in their python code, and build robust applications and software using small business & general ledger accounting data.
# Table of Contents
- [API Client documentation](#api-client-documentation)
- [Sample Applications](#sample-applications)
- [Xero Account Requirements](#xero-account-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Authentication](#authentication)
- [Custom Connections](#custom-connections)
- [App Store Subscriptions](#app-store-subscriptions)
- [API Clients](#api-clients)
- [Helper Methods](#helper-methods)
- [Usage Examples](#usage-examples)
- [SDK conventions](#sdk-conventions)
- [Participating in Xero’s developer community](#participating-in-xeros-developer-community)
- [Contributing](#contributing)

<hr>

## API Client documentation
This SDK supports full method coverage for the following Xero API sets:

| API Set | Description |
| --- | --- |
| [`Accounting`](https://xeroapi.github.io/xero-python/v1/accounting/index.html) | The Accounting API exposes accounting functions of the main Xero application *(most commonly used)*
| [Assets](https://xeroapi.github.io/xero-python/v1/assets/index.html) | The Assets API exposes fixed asset related functions of the Xero Accounting application |
| [Files](https://xeroapi.github.io/xero-python/v1/files/index.html) | The Files API provides access to the files, folders, and the association of files within a Xero organisation |
| [Projects](https://xeroapi.github.io/xero-python/v1/projects/index.html) | Xero Projects allows businesses to track time and costs on projects/jobs and report on profitability |
| [Payroll (AU)](https://xeroapi.github.io/xero-python/v1/payroll-au/index.html) | The (AU) Payroll API exposes payroll related functions of the payroll Xero application |
| [Payroll (UK)](https://xeroapi.github.io/xero-python/v1/payroll-uk/index.html) | The (UK) Payroll API exposes payroll related functions of the payroll Xero application |
| [Payroll (NZ)](https://xeroapi.github.io/xero-python/v1/payroll-nz/index.html) | The (NZ) Payroll API exposes payroll related functions of the payroll Xero application |

<img src="https://i.imgur.com/feMhCtI.png" alt="drawing" width="350"/>

<hr>

## Sample Applications
Sample apps can get you started quickly with simple auth flows and advanced usage examples.

| Sample App | Description | Screenshot |
| --- | --- | --- |
| [`starter-app`](https://github.com/XeroAPI/xero-python-oauth2-starter) | Basic getting started code samples | <img src="https://i.imgur.com/gJA93yT.png" alt="drawing" width="200"/>
| [`full-app`](https://github.com/XeroAPI/xero-python-oauth2-app) | Complete app with more complex examples | <img src="https://i.imgur.com/1YRqMmc.png" alt="drawing" width="500"/>
| [`custom-connections-starter`](https://github.com/XeroAPI/xero-python-custom-connections-starter) | Basic app showing Custom Connections - a Xero [premium option](https://developer.xero.com/documentation/oauth2/custom-connections) for building M2M integrations to a single org | <img src="https://i.imgur.com/uOlaWg8.png" alt="drawing" width="300"/>

<hr>

## Xero Account Requirements
- Create a [free Xero user account](https://www.xero.com/us/signup/api/)
- Login to your Xero developer [dashboard](https://developer.xero.com/app/manage) and create an API application
- Copy the credentials from your API app and store them using a secure ENV variable strategy
- Decide the [neccesary scopes](https://developer.xero.com/documentation/oauth2/scopes) for your app's functionality

# Installation
To install this SDK in your project:
```
pip install xero-python
```

---
## Configuration
```python
# -*- coding: utf-8 -*-
import os
from functools import wraps
from io import BytesIO
from logging.config import dictConfig
from flask import Flask, session
from flask_oauthlib.contrib.client import OAuth, OAuth2Application
from flask_session import Session
from xero_python.accounting import AccountingApi
from xero_python.assets import AssetApi
from xero_python.project import ProjectApi
from xero_python.payrollau import PayrollAuApi
from xero_python.payrolluk import PayrollUkApi
from xero_python.payrollnz import PayrollNzApi
from xero_python.file import FilesApi
from xero_python.api_client import ApiClient, serialize
from xero_python.api_client.configuration import Configuration
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import AccountingBadRequestException, PayrollUkBadRequestException
from xero_python.identity import IdentityApi
from xero_python.utils import getvalue
import logging_settings
from utils import jsonify, serialize_model

dictConfig(logging_settings.default_settings)

# configure main flask application
app = Flask(__name__)
app.config.from_object("default_settings")
app.config.from_pyfile("config.py", silent=True)

if app.config["ENV"] != "production":
    # allow oauth2 loop to run over http (used for local testing only)
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# configure persistent session cache
Session(app)

# configure flask-oauthlib application
oauth = OAuth(app)
xero = oauth.remote_app(
    name="xero",
    version="2",
    client_id=app.config["CLIENT_ID"],
    client_secret=app.config["CLIENT_SECRET"],
    endpoint_url="https://api.xero.com/",
    authorization_url="https://login.xero.com/identity/connect/authorize",
    access_token_url="https://identity.xero.com/connect/token",
    refresh_token_url="https://identity.xero.com/connect/token",
    scope="offline_access openid profile email accounting.transactions "
    "accounting.transactions.read accounting.reports.read "
    "accounting.journals.read accounting.settings accounting.settings.read "
    "accounting.contacts accounting.contacts.read accounting.attachments "
    "accounting.attachments.read assets projects "
    "files "
    "payroll.employees payroll.payruns payroll.payslip payroll.timesheets payroll.settings",
)  # type: OAuth2Application


# configure xero-python sdk client
api_client = ApiClient(
    Configuration(
        debug=app.config["DEBUG"],
        oauth2_token=OAuth2Token(
            client_id=app.config["CLIENT_ID"], client_secret=app.config["CLIENT_SECRET"]
        ),
    ),
    pool_threads=1,
)

# configure token persistence and exchange point between flask-oauthlib and xero-python
@xero.tokengetter
@api_client.oauth2_token_getter
def obtain_xero_oauth2_token():
    return session.get("token")

@xero.tokensaver
@api_client.oauth2_token_saver
def store_xero_oauth2_token(token):
    session["token"] = token
    session.modified = True
```

---
## Authentication
All API requests go through Xero's OAuth 2.0 gateway and require a valid `access_token` to be set on the `client` which appends the `access_token` [JWT](https://jwt.io/) to the header of each request.

If you are making an API call for the first time:

1. Send the user to the Xero authorization URL
```python
@app.route("/login")
def login():
    redirect_url = url_for("oauth_callback", _external=True)
    session["state"] = app.config["STATE"]
    try:
        response = xero.authorize(callback_uri=redirect_url, state=session["state"])
    except Exception as e:
        print(e)
        raise
    return response
```
2. The user will authorize your application and be sent to your `redirect_uri`. This is when and where to check that the returned "state" param matches that which was previously defined. If the "state" params match, calling the oauth library's `authorized_response()` method will swap the temporary auth code for an access token which you can store and use for subsequent API calls.
```python
@app.route("/callback")
def oauth_callback():
    if request.args.get("state") != session["state"]:
        return "Error, state doesn't match, no token for you."
    try:
        response = xero.authorized_response()
    except Exception as e:
        print(e)
        raise
    if response is None or response.get("access_token") is None:
        return "Access denied: response=%s" % response
    store_xero_oauth2_token(response)
    return redirect(url_for("index", _external=True))
```
3. Call the Xero API like so:
```python
@app.route("/accounting_invoice_read_all")
@xero_token_required
def accounting_invoice_read_all():
    code = get_code_snippet("INVOICES","READ_ALL")

    #[INVOICES:READ_ALL]
    xero_tenant_id = get_xero_tenant_id()
    accounting_api = AccountingApi(api_client)

    try:
        invoices_read = accounting_api.get_invoices(
            xero_tenant_id
        )
    except AccountingBadRequestException as exception:
        output = "Error: " + exception.reason
        json = jsonify(exception.error_data)
    else:
        output = "Total invoices found:  {}.".format(len(invoices_read.invoices)
        )
        json = serialize_model(invoices_read)
    #[/INVOICES:READ_ALL]

    return render_template(
        "output.html", title="Invoices",code=code, output=output, json=json, len = 0, set="accounting", endpoint="invoice", action="read_all"
    )
```

It is recommended that you store this token set JSON in a datastore in relation to the user who has authenticated the Xero API connection. Each time you want to call the Xero API, you will need to access the previously generated token set, initialize it on the SDK `client`, and refresh the `access_token` prior to making API calls.

### Token Set
| key | value | description |
| --- | --- | --- |
| id_token: | "xxx.yyy.zzz" | [OpenID Connect](https://openid.net/connect/) token returned if `openid profile email` scopes accepted |
| access_token: | "xxx.yyy.zzz" | [Bearer token](https://oauth.net/2/jwt/) with a 30 minute expiration required for all API calls |
| expires_in: | 1800 | Time in seconds till the token expires - 1800s is 30m |
| refresh_token: | "XXXXXXX" | Alphanumeric string used to obtain a new Token Set w/ a fresh access_token - 60 day expiry |
| scope: | ["email", "profile", "openid", "accounting.transactions", "offline_access"] | The Xero permissions that are embedded in the `access_token` |

Example Token Set JSON:
```
{
  "id_token": "xxx.yyy.zz",
  "access_token": "xxx.yyy.zzz",
  "expires_in": 1800,
  "token_type": "Bearer",
  "refresh_token": "xxxxxxxxx",
  "scope": ["email", "profile", "openid", "accounting.transactions", "offline_access"]
}
```

---
## Custom Connections

Custom Connections are a Xero [premium option](https://developer.xero.com/documentation/oauth2/custom-connections) used for building M2M integrations to a single organisation. A custom connection uses OAuth 2.0's [`client_credentials`](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/) grant which eliminates the step of exchanging the temporary code for a token set.

To use this SDK with a Custom Connections:
```python
# -*- coding: utf-8 -*-
import os
from functools import wraps
from io import BytesIO
from logging.config import dictConfig
from flask import Flask, url_for, render_template, session, redirect, json, send_file
from flask_session import Session
from xero_python.accounting import AccountingApi, ContactPerson, Contact, Contacts
from xero_python.api_client import ApiClient, serialize
from xero_python.api_client.configuration import Configuration
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import AccountingBadRequestException
from xero_python.identity import IdentityApi
from xero_python.utils import getvalue
import logging_settings
from utils import jsonify, serialize_model

dictConfig(logging_settings.default_settings)

# configure main flask application
app = Flask(__name__)
app.config.from_object("default_settings")
app.config.from_pyfile("config.py", silent=True)

# configure persistent session cache
Session(app)

# configure xero-python sdk client
api_client = ApiClient(
    Configuration(
        debug=app.config["DEBUG"],
        oauth2_token=OAuth2Token(
            client_id=app.config["CLIENT_ID"], client_secret=app.config["CLIENT_SECRET"]
        ),
    ),
    pool_threads=1,
)

# configure token persistence and exchange point between app session and xero-python
@api_client.oauth2_token_getter
def obtain_xero_oauth2_token():
    return session.get("token")

@api_client.oauth2_token_saver
def store_xero_oauth2_token(token):
    session["token"] = token
    session.modified = True

@app.route("/get_token")
def get_token():
    try:
        # no user auth flow, no exchanging temp code for token
        xero_token = api_client.get_client_credentials_token()
    except Exception as e:
        print(e)
        raise
    # todo validate state value
    if xero_token is None or xero_token.get("access_token") is None:
        return "Access denied: response=%s" % xero_token
    store_xero_oauth2_token(xero_token)
    return redirect(url_for("index", _external=True))

@app.route("/accounting_invoice_read_all")
@xero_token_required
def accounting_invoice_read_all():
    code = get_code_snippet("INVOICES","READ_ALL")

    #[INVOICES:READ_ALL]
    accounting_api = AccountingApi(api_client)

    try:
        invoices_read = accounting_api.get_invoices('')
    except AccountingBadRequestException as exception:
        output = "Error: " + exception.reason
        json = jsonify(exception.error_data)
    else:
        output = "Total invoices found:  {}.".format(len(invoices_read.invoices)
        )
        json = serialize_model(invoices_read)
    #[/INVOICES:READ_ALL]

    return render_template(
        "output.html", title="Invoices",code=code, output=output, json=json, len = 0, set="accounting", endpoint="invoice", action="read_all"
    )
```

Because Custom Connections are only valid for a single organisation you don't need to pass the xero-tenant-id as the first parameter to every method, or more specifically for this SDK xeroTenantId can be an empty string.

> Because the SDK is generated from the OpenAPI spec the parameter remains. For now you are required to pass an empty string to use this SDK with a Custom Connection.

---

## App Store Subscriptions

If you are implementing subscriptions to participate in Xero's App Store you will need to setup [App Store subscriptions](https://developer.xero.com/documentation/guides/how-to-guides/xero-app-store-referrals/) endpoints.

When a plan is successfully purchased, the user is redirected back to the URL specified in the setup process. The Xero App Store appends the subscription Id to this URL so you can immediately determine what plan the user has subscribed to through the subscriptions API.

With your app credentials you can create a client via `client_credentials` grant_type with the `marketplace.billing` scope. This unique access_token will allow you to query any functions in `AppStoreApi`. Client Credentials tokens to query app store endpoints will only work for apps that have completed the App Store on-boarding process.
```python
# configure xero-python sdk client
api_client = ApiClient(
    Configuration(
        debug=app.config["DEBUG"],
        oauth2_token=OAuth2Token(
            client_id=app.config["CLIENT_ID"], client_secret=app.config["CLIENT_SECRET"]
        ),
    ),
    pool_threads=1,
)

try:
    # pass True for app_store_billing - defaults to False if no value provided
    xero_token = api_client.get_client_credentials_token(True)
except Exception as e:
    print(e)
    raise

app_store_api = AppStoreApi(api_client)

subscription = app_store_api.get_subscription(subscription_id)
print(subscription)

{
  'current_period_end': datetime.datetime(2021, 9, 2, 14, 8, 58, 772536, tzinfo=tzutc()),
  'end_date': None,
  'id': '03bc74f2-1237-4477-b782-2dfb1a6d8b21',
  'organisation_id': '79e8b2e5-c63d-4dce-888f-e0f3e9eac647',
  'plans':[
    {
      'id': '6abc26f3-9390-4194-8b25-ce8b9942fda9',
      'name': 'Small',
      'status': 'ACTIVE',
      'subscription_items': [
        {
          'end_date': None,
          'id': '834cff4c-b753-4de2-9e7a-3451e14fa17a',
          'price': {
            'amount': Decimal('0.1000'),
            'currency': 'NZD',
            'id': '2310de92-c7c0-4bcb-b972-fb7612177bc7'
          },
          'product': {
            'id': '9586421f-7325-4493-bac9-d93be06a6a38',
            'name': '',
            'type': 'FIXED',
            'seat_unit': None
          },
          'start_date': datetime.datetime(2021, 8, 2, 14, 8, 58, 772536, tzinfo=tzutc()),
          'test_mode': True
        }
      ]
    }
  ],
  'start_date': datetime.datetime(2021, 8, 2, 14, 8, 58, 772536, tzinfo=tzutc()),
  'status': 'ACTIVE',
  'test_mode': True
}

```
You should use the subscription data to provision user access/permissions to your application.
### App Store Subscription Webhooks

In additon to a subscription Id being passed through the URL, when a purchase or an upgrade takes place you will be notified via a webhook. You can then use the subscription Id in the webhook payload to query the AppStore endpoints and determine what plan the user purchased, upgraded, downgraded or cancelled.

Refer to Xero's documenation to learn more about setting up and receiving webhooks.
> https://developer.xero.com/documentation/guides/webhooks/overview/

---
## API Clients
You can access the different API sets and their available methods through the following:

```python
accounting_api = AccountingApi(api_client)
read_accounts = accounting_api.get_accounts(xero_tenant_id)
asset_api = AssetApi(api_client)
read_assets = asset_api.get_assets(xero_tenant_id)
# ... all the API sets follow the same pattern
```
---
## Helper Methods

Once you have a valid Token Set in your datastore, the next time you want to call the Xero API simply initialize a new `client` and refresh the token set.

```python
# configure xero-python sdk client
api_client = ApiClient(
    Configuration(
        debug=app.config["DEBUG"],
        oauth2_token=OAuth2Token(
            client_id=app.config["CLIENT_ID"], client_secret=app.config["CLIENT_SECRET"]
        ),
    ),
    pool_threads=1,
)

# configure token persistence and exchange point between app session and xero-python
@api_client.oauth2_token_getter
def obtain_xero_oauth2_token():
    return session.get("token")

@api_client.oauth2_token_saver
def store_xero_oauth2_token(token):
    session["token"] = token
    session.modified = True

# get existing token set
token_set = get_token_set_from_database(user_id); // example function name

# set token set to the api client
store_xero_oauth2_token(token_set)

# refresh token set on the api client
api_client.refresh_oauth2_token()

# call the Xero API
accounting_api = AccountingApi(api_client)
read_accounts = accounting_api.get_accounts(xero_tenant_id)
```

A full list of the SDK client's methods:

| method | description | params | returns
| --- | --- | --- | --- |
| api_client.`oauth2_token_saver` | A decorator to register a callback function for saving refreshed token while the old token has expired | token_saver: the callback function accepting `token` argument | token_saver to allow this method be used as decorator |
| api_client.`oauth2_token_getter` | A decorator to register a callback function for getting oauth2 token | token_getter: the callback function returning oauth2 token dictionary | token_getter to allow this method be used as decorator |
| api_client.`revoke_oauth2_token` | Revokes a users refresh token and removes all their connections to your app | N/A | empty OAuth2 token |
| api_client.`refresh_oauth2_token` | Refreshes OAuth2 token set | N/A | new token set |
| api_client.`set_oauth2_token` | Sets OAuth2 token directly on the client | dict token: standard token dictionary | N/A |
| api_client.`get_oauth2_token` | Get OAuth2 token dictionary | N/A | dict |
---
## Usage Examples
### Accounting API
```python
from xero_python.accounting import AccountingApi
from xero_python.utils import getvalue

accounting_api = AccountingApi(api_client)

# Get Accounts
read_accounts = accounting_api.get_accounts(xero_tenant_id)
account_id = getvalue(read_accounts, "accounts.0.account_id", "")

# Get Account by ID
read_one_account = accounting_api.get_account(xero_tenant_id, account_id)

# Create Invoice
# get contact
read_contacts = accounting_api.get_contacts(xero_tenant_id)
contact_id = getvalue(read_contacts, "contacts.0.contact_id", "")
# get account
where = "Type==\"SALES\"&&Status==\"ACTIVE\""
read_accounts = accounting_api.get_accounts(
    xero_tenant_id, where=where
)
account_id = getvalue(read_accounts, "accounts.0.account_id", "")
# build Invoices
contact = Contact(
    contact_id=contact_id
)
line_item = LineItem(
    account_code=account_id,
    description= "Consulting",
    quantity=1.0,
    unit_amount=10.0,
)
invoice = Invoice(
    line_items=[line_item],
    contact=contact,
    due_date= dateutil.parser.parse("2020-09-03T00:00:00Z"),
    date= dateutil.parser.parse("2020-07-03T00:00:00Z"),
    type="ACCREC"
)
invoices = Invoices(invoices=[invoice])
created_invoices = accounting_api.create_invoices(xero_tenant_id, invoices=invoices)
invoice_id = getvalue(read_invoices, "invoices.0.invoice_id", "")

# Create Attachment
include_online = True
file_name = "helo-heros.jpg"
path_to_upload = Path(__file__).resolve().parent.joinpath(file_name)
open_file = open(path_to_upload, 'rb')
body = open_file.read()
content_type = mimetypes.MimeTypes().guess_type(file_name)[0]

created_invoice_attachments_by_file_name = accounting_api.create_invoice_attachment_by_file_name(
    xero_tenant_id,
    invoice_id,
    file_name,
    body,
    include_online,
)
```

---
## SDK conventions

### Querying & Filtering

Describe the support for query options and filtering

```python
# configure api_client for use with xero-python sdk client
api_client = ApiClient(
    Configuration(
        debug=false,
        oauth2_token=OAuth2Token(
            client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
        ),
    ),
    pool_threads=1,
)

api_client.set_oauth2_token("YOUR_ACCESS_TOKEN")

def accounting_get_invoices():
    api_instance = AccountingApi(api_client)
    xero_tenant_id = 'YOUR_XERO_TENANT_ID'
    if_modified_since = dateutil.parser.parse("2020-02-06T12:17:43.202-08:00")
    where = 'Status=="DRAFT"'
    order = 'InvoiceNumber ASC'
    ids = ["00000000-0000-0000-0000-000000000000"]
    invoice_numbers = ["INV-001", "INV-002"]
    contact_ids = ["00000000-0000-0000-0000-000000000000"]
    statuses = ["DRAFT", "SUBMITTED"]
    include_archived = 'true'
    created_by_my_app = 'false'
    summary_only = 'true'

api_response = api_instance.get_invoices(
    xero_tenant_id,
    if_modified_since,
    where,
    order,
    ids,
    invoice_numbers,
    contact_ids,
    statuses,
    page,
    include_archived,
    created_by_my_app,
    unitdp,
    summary_only
)
```

---

## Participating in Xero’s developer community

This SDK is one of a number of SDK’s that the Xero Developer team builds and maintains. We are grateful for all the contributions that the community makes.

Here are a few things you should be aware of as a contributor:
* Xero has adopted the Contributor Covenant [Code of Conduct](https://github.com/XeroAPI/xero-python/blob/master/CODE_OF_CONDUCT.md), we expect all contributors in our community to adhere to it
* If you raise an issue then please make sure to fill out the Github issue template, doing so helps us help you
* You’re welcome to raise PRs. As our SDKs are generated we may use your code in the core SDK build instead of merging your code
* We have a [contribution guide](https://github.com/XeroAPI/xero-python/blob/master/CONTRIBUTING.md) for you to follow when contributing to this SDK
* Curious about how we generate our SDK’s? Have a [read of our process](https://devblog.xero.com/building-sdks-for-the-future-b79ff726dfd6) and have a look at our [OpenAPISpec](https://github.com/XeroAPI/Xero-OpenAPI)
* This software is published under the [MIT License](https://github.com/XeroAPI/xero-python/blob/master/LICENSE)

For questions that aren’t related to SDKs please refer to our [developer support page](https://developer.xero.com/support/).

### Contributing
PRs, issues, and discussion are highly appreciated and encouraged. Note that the majority of this project is generated code based on [Xero's OpenAPI specs](https://github.com/XeroAPI/Xero-OpenAPI) - PR's will be evaluated and pre-merge will be incorporated into the root generation templates.

### Versioning
We do our best to keep OS industry `semver` standards, but we can make mistakes! If something is not accurately reflected in a version's release notes please let the team know.
