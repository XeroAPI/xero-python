# -*- coding: utf-8 -*-
"""
Tests for xero_python.models.BaseModel.to_dict serialization.

Regression test for #93: BaseModel.to_dict() must return JSON-serializable
primitives. Previously enum-typed (and UUID-typed) attributes were returned
as the raw Enum / UUID object, so json.dumps(model.to_dict()) raised.
"""
import json
from enum import Enum
from uuid import UUID

from xero_python.models import BaseModel


class AccountType(Enum):
    BANK = "BANK"
    EXPENSE = "EXPENSE"


class Journal(BaseModel):
    openapi_types = {"account_type": "AccountType", "journal_id": "UUID", "name": "str"}
    attribute_map = {
        "account_type": "AccountType",
        "journal_id": "JournalID",
        "name": "Name",
    }

    def __init__(self, **kwargs):
        # mirror generated models: every declared attribute defaults to None
        for name in self.openapi_types:
            setattr(self, name, None)
        for name, value in kwargs.items():
            setattr(self, name, value)


def test_to_dict_serializes_enum_to_its_value():
    journal = Journal(account_type=AccountType.BANK)
    assert journal.to_dict()["account_type"] == "BANK"


def test_to_dict_serializes_uuid_to_string():
    journal = Journal(journal_id=UUID("12345678-1234-5678-1234-567812345678"))
    assert journal.to_dict()["journal_id"] == "12345678-1234-5678-1234-567812345678"


def test_to_dict_is_json_serializable():
    journal = Journal(
        account_type=AccountType.EXPENSE,
        journal_id=UUID("12345678-1234-5678-1234-567812345678"),
        name="Sales",
    )
    # should not raise
    encoded = json.dumps(journal.to_dict())
    assert json.loads(encoded) == {
        "account_type": "EXPENSE",
        "journal_id": "12345678-1234-5678-1234-567812345678",
        "name": "Sales",
    }
