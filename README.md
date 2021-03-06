# xero-python

[![image](https://img.shields.io/pypi/v/xero-python.svg)](https://pypi.python.org/pypi/xero-python)

<!-- [![image](https://img.shields.io/travis/xero-github/xero-python.svg)](https://travis-ci.com/xero-github/xero-python) -->

<!-- [![Documentation Status](https://readthedocs.org/projects/xero-python/badge/?version=latest)](https://xero-python.readthedocs.io/en/latest/?badge=latest) -->

<!--  *   Documentation: <https://xero-python.readthedocs.io>. -->

Official python SDK for Xero API generated by OpenAPI spec for oAuth 2

## Features

* XERO API Client with oauth2 token integration.
* Automatic OAuth 2 token refresh before token expiration.
* Class based interface for Xero API endpoints.
* Model classes used to represent API data.
* Currently Supported API sets:

    * [Accounting API](https://developer.xero.com/documentation/api/api-overview)
    * [Assets API](https://developer.xero.com/documentation/assets-api/overview)
    * [Files API](https://developer.xero.com/documentation/files-api/overview-files)
    * [Payroll API (AU)](https://developer.xero.com/documentation/payroll-api/overview)
    * [Payroll API (NZ)](https://developer.xero.com/documentation/payroll-api-nz/overview)
    * [Payroll API (UK)](https://developer.xero.com/documentation/payroll-api-uk/overview)
    * [Projects API](https://developer.xero.com/documentation/projects/overview-projects)
    
* Error handling for ease of use.

## SDK Documentation
* [Accounting](https://xeroapi.github.io/xero-python/v1/accounting/index.html)

## Starter Project
We've created [xero-python-outh2-starter](https://github.com/XeroAPI/xero-python-oauth2-starter) a project to demonstrate how to use this SDK.

* oauth 2 flow to obtain a token
* token refresh
* identity to obtain tenant_id
* organisation endpoint
* create contact
* create multiple contacts
* get invoices using where clause

Here is a [15 min video walkthrough](https://www.youtube.com/watch?v=i8JWtbMo90M) on using the starter project.

## Kitchen Sync app
We've created [xero-python-outh2-app](https://github.com/XeroAPI/xero-python-oauth2-app) a project to demonstrate how to make API calls and displays the python code used to make the call and the JSON response.

* oauth 2 flow to obtain a token
* token refresh
* identity to obtain tenant_id
* accounting
    * accounts
    * contacts
    * invoices
* assets
    * asset
    * asset type
    * asset settings
* projects
    * projects
    * project users
    * tasks
    * time
* au payroll
    * employee
    * leave applications
    * pay items
    * payroll calendar
    * pay runs
    * pay slips
    * settings
    * superfunds
    * superfund products
    * timesheets
* uk payroll
    * employees
    * employement
    * employees tax
    * employee opening balance
    * employees leave
    * employees leave balances
    * employees statutory leave balances
    * employees statutory leave summary
    * employees statutory sick leave
    * employees leave periods
    * employees leave types
    * employees pay templates
    * employer pensions
    * deductions
    * earnings orders
    * earnings rates
    * leave types
    * reimbursements
    * timesheets
    * payment methods
    * payrun calendars
    * salary and wage
    * pay runs
    * pay slips
    * settings
    * tracking categories

## Credits

* This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.

## Participating in Xero’s developer community
This SDK is one of a number of SDK’s that the Xero Developer team builds and maintains. We are grateful for all the contributions that the community makes. 

Here are a few things you should be aware of as a contributor:
* Xero has adopted the Contributor Covenant [Code of Conduct](https://github.com/XeroAPI/xero-python/blob/master/CODE_OF_CONDUCT.md), we expect all contributors in our community to adhere to it
* If you raise an issue then please make sure to fill out the github issue template, doing so helps us help you 
* You’re welcome to raise PRs. As our SDKs are generated we may use your code in the core SDK build instead of merging your code
* We have a [contribution guide](https://github.com/XeroAPI/xero-python/blob/master/CONTRIBUTING.md) for you to follow when contributing to this SDK
* Curious about how we generate our SDK’s? Have a [read of our process](https://devblog.xero.com/building-sdks-for-the-future-b79ff726dfd6) and have a look at our [OpenAPISpec](https://github.com/XeroAPI/Xero-OpenAPI)
* This software is published under the [MIT License](https://github.com/XeroAPI/xero-python/blob/master/LICENSE)

For questions that aren’t related to SDKs please refer to our [developer support page](https://developer.xero.com/support/).
