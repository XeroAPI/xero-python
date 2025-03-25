# coding: utf-8

"""
Xero Finance API

The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class StatementResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "statement_id": "str",
        "start_date": "date",
        "end_date": "date",
        "imported_date_time_utc": "datetime",
        "import_source": "str",
        "start_balance": "float",
        "end_balance": "float",
        "indicative_start_balance": "float",
        "indicative_end_balance": "float",
        "statement_lines": "list[StatementLineResponse]",
    }

    attribute_map = {
        "statement_id": "statementId",
        "start_date": "startDate",
        "end_date": "endDate",
        "imported_date_time_utc": "importedDateTimeUtc",
        "import_source": "importSource",
        "start_balance": "startBalance",
        "end_balance": "endBalance",
        "indicative_start_balance": "indicativeStartBalance",
        "indicative_end_balance": "indicativeEndBalance",
        "statement_lines": "statementLines",
    }

    def __init__(
        self,
        statement_id=None,
        start_date=None,
        end_date=None,
        imported_date_time_utc=None,
        import_source=None,
        start_balance=None,
        end_balance=None,
        indicative_start_balance=None,
        indicative_end_balance=None,
        statement_lines=None,
    ):  # noqa: E501
        """StatementResponse - a model defined in OpenAPI"""  # noqa: E501

        self._statement_id = None
        self._start_date = None
        self._end_date = None
        self._imported_date_time_utc = None
        self._import_source = None
        self._start_balance = None
        self._end_balance = None
        self._indicative_start_balance = None
        self._indicative_end_balance = None
        self._statement_lines = None
        self.discriminator = None

        if statement_id is not None:
            self.statement_id = statement_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if imported_date_time_utc is not None:
            self.imported_date_time_utc = imported_date_time_utc
        if import_source is not None:
            self.import_source = import_source
        if start_balance is not None:
            self.start_balance = start_balance
        if end_balance is not None:
            self.end_balance = end_balance
        if indicative_start_balance is not None:
            self.indicative_start_balance = indicative_start_balance
        if indicative_end_balance is not None:
            self.indicative_end_balance = indicative_end_balance
        if statement_lines is not None:
            self.statement_lines = statement_lines

    @property
    def statement_id(self):
        """Gets the statement_id of this StatementResponse.  # noqa: E501

        Xero Identifier of statement  # noqa: E501

        :return: The statement_id of this StatementResponse.  # noqa: E501
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        """Sets the statement_id of this StatementResponse.

        Xero Identifier of statement  # noqa: E501

        :param statement_id: The statement_id of this StatementResponse.  # noqa: E501
        :type: str
        """

        self._statement_id = statement_id

    @property
    def start_date(self):
        """Gets the start_date of this StatementResponse.  # noqa: E501

        Start date of statement  # noqa: E501

        :return: The start_date of this StatementResponse.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this StatementResponse.

        Start date of statement  # noqa: E501

        :param start_date: The start_date of this StatementResponse.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this StatementResponse.  # noqa: E501

        End date of statement  # noqa: E501

        :return: The end_date of this StatementResponse.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this StatementResponse.

        End date of statement  # noqa: E501

        :param end_date: The end_date of this StatementResponse.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def imported_date_time_utc(self):
        """Gets the imported_date_time_utc of this StatementResponse.  # noqa: E501

        Utc date time of when the statement was imported in Xero  # noqa: E501

        :return: The imported_date_time_utc of this StatementResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._imported_date_time_utc

    @imported_date_time_utc.setter
    def imported_date_time_utc(self, imported_date_time_utc):
        """Sets the imported_date_time_utc of this StatementResponse.

        Utc date time of when the statement was imported in Xero  # noqa: E501

        :param imported_date_time_utc: The imported_date_time_utc of this StatementResponse.  # noqa: E501
        :type: datetime
        """

        self._imported_date_time_utc = imported_date_time_utc

    @property
    def import_source(self):
        """Gets the import_source of this StatementResponse.  # noqa: E501

        Identifies where the statement data in Xero was sourced, 1) direct bank feed, automatically loaded from the bank (eg STMTIMPORTSRC/CBAFEED); 2) indirect bank feed, automatically loaded from a 3rd party provider (eg STMTIMPORTSRC/YODLEE); 3) manually uploaded bank feed (eg STMTIMPORTSRC/CSV) or 4) manually entered statement data (STMTIMPORTSRC/MANUAL).  # noqa: E501

        :return: The import_source of this StatementResponse.  # noqa: E501
        :rtype: str
        """
        return self._import_source

    @import_source.setter
    def import_source(self, import_source):
        """Sets the import_source of this StatementResponse.

        Identifies where the statement data in Xero was sourced, 1) direct bank feed, automatically loaded from the bank (eg STMTIMPORTSRC/CBAFEED); 2) indirect bank feed, automatically loaded from a 3rd party provider (eg STMTIMPORTSRC/YODLEE); 3) manually uploaded bank feed (eg STMTIMPORTSRC/CSV) or 4) manually entered statement data (STMTIMPORTSRC/MANUAL).  # noqa: E501

        :param import_source: The import_source of this StatementResponse.  # noqa: E501
        :type: str
        """

        self._import_source = import_source

    @property
    def start_balance(self):
        """Gets the start_balance of this StatementResponse.  # noqa: E501

        Opening balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. Where not supplied, the value will be 0.  # noqa: E501

        :return: The start_balance of this StatementResponse.  # noqa: E501
        :rtype: float
        """
        return self._start_balance

    @start_balance.setter
    def start_balance(self, start_balance):
        """Sets the start_balance of this StatementResponse.

        Opening balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. Where not supplied, the value will be 0.  # noqa: E501

        :param start_balance: The start_balance of this StatementResponse.  # noqa: E501
        :type: float
        """

        self._start_balance = start_balance

    @property
    def end_balance(self):
        """Gets the end_balance of this StatementResponse.  # noqa: E501

        Closing balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. Where not supplied, the value will be 0.  # noqa: E501

        :return: The end_balance of this StatementResponse.  # noqa: E501
        :rtype: float
        """
        return self._end_balance

    @end_balance.setter
    def end_balance(self, end_balance):
        """Sets the end_balance of this StatementResponse.

        Closing balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. Where not supplied, the value will be 0.  # noqa: E501

        :param end_balance: The end_balance of this StatementResponse.  # noqa: E501
        :type: float
        """

        self._end_balance = end_balance

    @property
    def indicative_start_balance(self):
        """Gets the indicative_start_balance of this StatementResponse.  # noqa: E501

        Opening statement balance calculated in Xero (= bank account conversion balance plus sum of imported bank statement lines). Note: If indicative statement balance doesn't match imported statement balance for the same date, either the conversion (opening at inception) balance in Xero is wrong or there's an error in the bank statement lines in Xero. Ref: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance?userregion=true   # noqa: E501

        :return: The indicative_start_balance of this StatementResponse.  # noqa: E501
        :rtype: float
        """
        return self._indicative_start_balance

    @indicative_start_balance.setter
    def indicative_start_balance(self, indicative_start_balance):
        """Sets the indicative_start_balance of this StatementResponse.

        Opening statement balance calculated in Xero (= bank account conversion balance plus sum of imported bank statement lines). Note: If indicative statement balance doesn't match imported statement balance for the same date, either the conversion (opening at inception) balance in Xero is wrong or there's an error in the bank statement lines in Xero. Ref: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance?userregion=true   # noqa: E501

        :param indicative_start_balance: The indicative_start_balance of this StatementResponse.  # noqa: E501
        :type: float
        """

        self._indicative_start_balance = indicative_start_balance

    @property
    def indicative_end_balance(self):
        """Gets the indicative_end_balance of this StatementResponse.  # noqa: E501

        Closing statement balance calculated in Xero (= bank account conversion balance plus sum of imported bank statement lines). Note: If indicative statement balance doesn't match imported statement balance for the same date, either the conversion (opening at inception) balance in Xero is wrong or there's an error in the bank statement lines in Xero. Ref: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance?userregion=true    # noqa: E501

        :return: The indicative_end_balance of this StatementResponse.  # noqa: E501
        :rtype: float
        """
        return self._indicative_end_balance

    @indicative_end_balance.setter
    def indicative_end_balance(self, indicative_end_balance):
        """Sets the indicative_end_balance of this StatementResponse.

        Closing statement balance calculated in Xero (= bank account conversion balance plus sum of imported bank statement lines). Note: If indicative statement balance doesn't match imported statement balance for the same date, either the conversion (opening at inception) balance in Xero is wrong or there's an error in the bank statement lines in Xero. Ref: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance?userregion=true    # noqa: E501

        :param indicative_end_balance: The indicative_end_balance of this StatementResponse.  # noqa: E501
        :type: float
        """

        self._indicative_end_balance = indicative_end_balance

    @property
    def statement_lines(self):
        """Gets the statement_lines of this StatementResponse.  # noqa: E501

        List of statement lines  # noqa: E501

        :return: The statement_lines of this StatementResponse.  # noqa: E501
        :rtype: list[StatementLineResponse]
        """
        return self._statement_lines

    @statement_lines.setter
    def statement_lines(self, statement_lines):
        """Sets the statement_lines of this StatementResponse.

        List of statement lines  # noqa: E501

        :param statement_lines: The statement_lines of this StatementResponse.  # noqa: E501
        :type: list[StatementLineResponse]
        """

        self._statement_lines = statement_lines
