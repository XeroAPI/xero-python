from xero.models import BaseModel


class Organisation(BaseModel):
    openapi_types = {
        "organisation_id": "str",
        "api_key": "str",
        "name": "str",
        "legal_name": "str",
        "pays_tax": "bool",
        "version": "str",
        "organisation_type": "str",
        "base_currency": "CurrencyCode",
        "country_code": "CountryCode",
        "is_demo_company": "bool",
        "organisation_status": "str",
        "registration_number": "str",
        "employer_identification_number": "str",
        "tax_number": "str",
        "financial_year_end_day": "int",
        "financial_year_end_month": "int",
        "sales_tax_basis": "str",
        "sales_tax_period": "str",
        "default_sales_tax": "str",
        "default_purchases_tax": "str",
        "period_lock_date": "date[ms-format]",
        "end_of_year_lock_date": "date[ms-format]",
        "created_date_utc": "datetime[ms-format]",
        "timezone": "TimeZone",
        "organisation_entity_type": "str",
        "short_code": "str",
        "_class": "str",
        "edition": "str",
        "line_of_business": "str",
        "addresses": "list[AddressForOrganisation]",
        "phones": "list[Phone]",
        "external_links": "list[ExternalLink]",
        "payment_terms": "PaymentTerm",
    }
    attribute_map = {
        "organisation_id": "OrganisationID",
        "api_key": "APIKey",
        "name": "Name",
        "legal_name": "LegalName",
        "pays_tax": "PaysTax",
        "version": "Version",
        "organisation_type": "OrganisationType",
        "base_currency": "BaseCurrency",
        "country_code": "CountryCode",
        "is_demo_company": "IsDemoCompany",
        "organisation_status": "OrganisationStatus",
        "registration_number": "RegistrationNumber",
        "employer_identification_number": "EmployerIdentificationNumber",
        "tax_number": "TaxNumber",
        "financial_year_end_day": "FinancialYearEndDay",
        "financial_year_end_month": "FinancialYearEndMonth",
        "sales_tax_basis": "SalesTaxBasis",
        "sales_tax_period": "SalesTaxPeriod",
        "default_sales_tax": "DefaultSalesTax",
        "default_purchases_tax": "DefaultPurchasesTax",
        "period_lock_date": "PeriodLockDate",
        "end_of_year_lock_date": "EndOfYearLockDate",
        "created_date_utc": "CreatedDateUTC",
        "timezone": "Timezone",
        "organisation_entity_type": "OrganisationEntityType",
        "short_code": "ShortCode",
        "_class": "Class",
        "edition": "Edition",
        "line_of_business": "LineOfBusiness",
        "addresses": "Addresses",
        "phones": "Phones",
        "external_links": "ExternalLinks",
        "payment_terms": "PaymentTerms",
    }

    def __init__(
        self,
        organisation_id=None,
        api_key=None,
        name=None,
        legal_name=None,
        pays_tax=None,
        version=None,
        organisation_type=None,
        base_currency=None,
        country_code=None,
        is_demo_company=None,
        organisation_status=None,
        registration_number=None,
        employer_identification_number=None,
        tax_number=None,
        financial_year_end_day=None,
        financial_year_end_month=None,
        sales_tax_basis=None,
        sales_tax_period=None,
        default_sales_tax=None,
        default_purchases_tax=None,
        period_lock_date=None,
        end_of_year_lock_date=None,
        created_date_utc=None,
        timezone=None,
        organisation_entity_type=None,
        short_code=None,
        _class=None,
        edition=None,
        line_of_business=None,
        addresses=None,
        phones=None,
        external_links=None,
        payment_terms=None,
    ):
        self._organisation_id = None
        self._api_key = None
        self._name = None
        self._legal_name = None
        self._pays_tax = None
        self._version = None
        self._organisation_type = None
        self._base_currency = None
        self._country_code = None
        self._is_demo_company = None
        self._organisation_status = None
        self._registration_number = None
        self._employer_identification_number = None
        self._tax_number = None
        self._financial_year_end_day = None
        self._financial_year_end_month = None
        self._sales_tax_basis = None
        self._sales_tax_period = None
        self._default_sales_tax = None
        self._default_purchases_tax = None
        self._period_lock_date = None
        self._end_of_year_lock_date = None
        self._created_date_utc = None
        self._timezone = None
        self._organisation_entity_type = None
        self._short_code = None
        self.__class = None
        self._edition = None
        self._line_of_business = None
        self._addresses = None
        self._phones = None
        self._external_links = None
        self._payment_terms = None
        self.discriminator = None
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if api_key is not None:
            self.api_key = api_key
        if name is not None:
            self.name = name
        if legal_name is not None:
            self.legal_name = legal_name
        if pays_tax is not None:
            self.pays_tax = pays_tax
        if version is not None:
            self.version = version
        if organisation_type is not None:
            self.organisation_type = organisation_type
        if base_currency is not None:
            self.base_currency = base_currency
        if country_code is not None:
            self.country_code = country_code
        if is_demo_company is not None:
            self.is_demo_company = is_demo_company
        if organisation_status is not None:
            self.organisation_status = organisation_status
        if registration_number is not None:
            self.registration_number = registration_number
        if employer_identification_number is not None:
            self.employer_identification_number = employer_identification_number
        if tax_number is not None:
            self.tax_number = tax_number
        if financial_year_end_day is not None:
            self.financial_year_end_day = financial_year_end_day
        if financial_year_end_month is not None:
            self.financial_year_end_month = financial_year_end_month
        if sales_tax_basis is not None:
            self.sales_tax_basis = sales_tax_basis
        if sales_tax_period is not None:
            self.sales_tax_period = sales_tax_period
        if default_sales_tax is not None:
            self.default_sales_tax = default_sales_tax
        if default_purchases_tax is not None:
            self.default_purchases_tax = default_purchases_tax
        if period_lock_date is not None:
            self.period_lock_date = period_lock_date
        if end_of_year_lock_date is not None:
            self.end_of_year_lock_date = end_of_year_lock_date
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if timezone is not None:
            self.timezone = timezone
        if organisation_entity_type is not None:
            self.organisation_entity_type = organisation_entity_type
        if short_code is not None:
            self.short_code = short_code
        if _class is not None:
            self._class = _class
        if edition is not None:
            self.edition = edition
        if line_of_business is not None:
            self.line_of_business = line_of_business
        if addresses is not None:
            self.addresses = addresses
        if phones is not None:
            self.phones = phones
        if external_links is not None:
            self.external_links = external_links
        if payment_terms is not None:
            self.payment_terms = payment_terms

    @property
    def organisation_id(self):
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        self._organisation_id = organisation_id

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        self._legal_name = legal_name

    @property
    def pays_tax(self):
        return self._pays_tax

    @pays_tax.setter
    def pays_tax(self, pays_tax):
        self._pays_tax = pays_tax

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        allowed_values = [
            "AU",
            "NZ",
            "GLOBAL",
            "UK",
            "US",
            "AUONRAMP",
            "NZONRAMP",
            "GLOBALONRAMP",
            "UKONRAMP",
            "USONRAMP",
            "None",
        ]
        if version:
            if version not in allowed_values:
                raise ValueError(
                    "Invalid value for `version` ({0}), must be one of {1}".format(
                        version, allowed_values
                    )
                )
        self._version = version

    @property
    def organisation_type(self):
        return self._organisation_type

    @organisation_type.setter
    def organisation_type(self, organisation_type):
        allowed_values = [
            "ACCOUNTING_PRACTICE",
            "COMPANY",
            "CHARITY",
            "CLUB_OR_SOCIETY",
            "INDIVIDUAL",
            "LOOK_THROUGH_COMPANY",
            "NOT_FOR_PROFIT",
            "PARTNERSHIP",
            "S_CORPORATION",
            "SELF_MANAGED_SUPERANNUATION_FUND",
            "SOLE_TRADER",
            "SUPERANNUATION_FUND",
            "TRUST",
            "None",
        ]
        if organisation_type:
            if organisation_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `organisation_type` ({0}), must be one of {1}".format(
                        organisation_type, allowed_values
                    )
                )
        self._organisation_type = organisation_type

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        self._base_currency = base_currency

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        self._country_code = country_code

    @property
    def is_demo_company(self):
        return self._is_demo_company

    @is_demo_company.setter
    def is_demo_company(self, is_demo_company):
        self._is_demo_company = is_demo_company

    @property
    def organisation_status(self):
        return self._organisation_status

    @organisation_status.setter
    def organisation_status(self, organisation_status):
        self._organisation_status = organisation_status

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        self._registration_number = registration_number

    @property
    def employer_identification_number(self):
        return self._employer_identification_number

    @employer_identification_number.setter
    def employer_identification_number(self, employer_identification_number):
        self._employer_identification_number = employer_identification_number

    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        self._tax_number = tax_number

    @property
    def financial_year_end_day(self):
        return self._financial_year_end_day

    @financial_year_end_day.setter
    def financial_year_end_day(self, financial_year_end_day):
        self._financial_year_end_day = financial_year_end_day

    @property
    def financial_year_end_month(self):
        return self._financial_year_end_month

    @financial_year_end_month.setter
    def financial_year_end_month(self, financial_year_end_month):
        self._financial_year_end_month = financial_year_end_month

    @property
    def sales_tax_basis(self):
        return self._sales_tax_basis

    @sales_tax_basis.setter
    def sales_tax_basis(self, sales_tax_basis):
        allowed_values = [
            "PAYMENTS",
            "INVOICE",
            "NONE",
            "CASH",
            "ACCRUAL",
            "FLATRATECASH",
            "FLATRATEACCRUAL",
            "ACCRUALS",
            "None",
        ]
        if sales_tax_basis:
            if sales_tax_basis not in allowed_values:
                raise ValueError(
                    "Invalid value for `sales_tax_basis` ({0}), must be one of {1}".format(
                        sales_tax_basis, allowed_values
                    )
                )
        self._sales_tax_basis = sales_tax_basis

    @property
    def sales_tax_period(self):
        return self._sales_tax_period

    @sales_tax_period.setter
    def sales_tax_period(self, sales_tax_period):
        allowed_values = [
            "MONTHLY",
            "QUARTERLY1",
            "QUARTERLY2",
            "QUARTERLY3",
            "ANNUALLY",
            "ONEMONTHS",
            "TWOMONTHS",
            "SIXMONTHS",
            "1MONTHLY",
            "2MONTHLY",
            "3MONTHLY",
            "6MONTHLY",
            "QUARTERLY",
            "YEARLY",
            "NONE",
            "None",
        ]
        if sales_tax_period:
            if sales_tax_period not in allowed_values:
                raise ValueError(
                    "Invalid value for `sales_tax_period` ({0}), must be one of {1}".format(
                        sales_tax_period, allowed_values
                    )
                )
        self._sales_tax_period = sales_tax_period

    @property
    def default_sales_tax(self):
        return self._default_sales_tax

    @default_sales_tax.setter
    def default_sales_tax(self, default_sales_tax):
        self._default_sales_tax = default_sales_tax

    @property
    def default_purchases_tax(self):
        return self._default_purchases_tax

    @default_purchases_tax.setter
    def default_purchases_tax(self, default_purchases_tax):
        self._default_purchases_tax = default_purchases_tax

    @property
    def period_lock_date(self):
        return self._period_lock_date

    @period_lock_date.setter
    def period_lock_date(self, period_lock_date):
        self._period_lock_date = period_lock_date

    @property
    def end_of_year_lock_date(self):
        return self._end_of_year_lock_date

    @end_of_year_lock_date.setter
    def end_of_year_lock_date(self, end_of_year_lock_date):
        self._end_of_year_lock_date = end_of_year_lock_date

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        self._timezone = timezone

    @property
    def organisation_entity_type(self):
        return self._organisation_entity_type

    @organisation_entity_type.setter
    def organisation_entity_type(self, organisation_entity_type):
        allowed_values = [
            "ACCOUNTING_PRACTICE",
            "COMPANY",
            "CHARITY",
            "CLUB_OR_SOCIETY",
            "INDIVIDUAL",
            "LOOK_THROUGH_COMPANY",
            "NOT_FOR_PROFIT",
            "PARTNERSHIP",
            "S_CORPORATION",
            "SELF_MANAGED_SUPERANNUATION_FUND",
            "SOLE_TRADER",
            "SUPERANNUATION_FUND",
            "TRUST",
            "None",
        ]
        if organisation_entity_type:
            if organisation_entity_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `organisation_entity_type` ({0}), must be one of {1}".format(
                        organisation_entity_type, allowed_values
                    )
                )
        self._organisation_entity_type = organisation_entity_type

    @property
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        self._short_code = short_code

    @property
    def _class(self):
        return self.__class

    @_class.setter
    def _class(self, _class):
        allowed_values = [
            "DEMO",
            "TRIAL",
            "STARTER",
            "STANDARD",
            "PREMIUM",
            "PREMIUM_20",
            "PREMIUM_50",
            "PREMIUM_100",
            "LEDGER",
            "GST_CASHBOOK",
            "NON_GST_CASHBOOK",
            "ULTIMATE",
            "LITE",
            "ULTIMATE_10",
            "ULTIMATE_20",
            "ULTIMATE_50",
            "ULTIMATE_100",
            "IGNITE",
            "GROW",
            "COMPREHENSIVE",
            "SIMPLE",
            "None",
        ]
        if _class:
            if _class not in allowed_values:
                raise ValueError(
                    "Invalid value for `_class` ({0}), must be one of {1}".format(
                        _class, allowed_values
                    )
                )
        self.__class = _class

    @property
    def edition(self):
        return self._edition

    @edition.setter
    def edition(self, edition):
        allowed_values = ["BUSINESS", "PARTNER", "None"]
        if edition:
            if edition not in allowed_values:
                raise ValueError(
                    "Invalid value for `edition` ({0}), must be one of {1}".format(
                        edition, allowed_values
                    )
                )
        self._edition = edition

    @property
    def line_of_business(self):
        return self._line_of_business

    @line_of_business.setter
    def line_of_business(self, line_of_business):
        self._line_of_business = line_of_business

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        self._addresses = addresses

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, phones):
        self._phones = phones

    @property
    def external_links(self):
        return self._external_links

    @external_links.setter
    def external_links(self, external_links):
        self._external_links = external_links

    @property
    def payment_terms(self):
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        self._payment_terms = payment_terms
