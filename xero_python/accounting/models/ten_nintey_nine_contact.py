# coding: utf-8

"""
Accounting API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.2.7
Contact: api@xero.com
Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TenNinteyNineContact(BaseModel):
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
        "box1": "float",
        "box2": "float",
        "box3": "float",
        "box4": "float",
        "box5": "float",
        "box6": "float",
        "box7": "float",
        "box8": "float",
        "box9": "float",
        "box10": "float",
        "box11": "float",
        "box13": "float",
        "box14": "float",
        "name": "str",
        "federal_tax_id_type": "str",
        "city": "str",
        "zip": "str",
        "state": "str",
        "email": "str",
        "street_address": "str",
        "tax_id": "str",
        "contact_id": "str",
    }

    attribute_map = {
        "box1": "Box1",
        "box2": "Box2",
        "box3": "Box3",
        "box4": "Box4",
        "box5": "Box5",
        "box6": "Box6",
        "box7": "Box7",
        "box8": "Box8",
        "box9": "Box9",
        "box10": "Box10",
        "box11": "Box11",
        "box13": "Box13",
        "box14": "Box14",
        "name": "Name",
        "federal_tax_id_type": "FederalTaxIDType",
        "city": "City",
        "zip": "Zip",
        "state": "State",
        "email": "Email",
        "street_address": "StreetAddress",
        "tax_id": "TaxID",
        "contact_id": "ContactId",
    }

    def __init__(
        self,
        box1=None,
        box2=None,
        box3=None,
        box4=None,
        box5=None,
        box6=None,
        box7=None,
        box8=None,
        box9=None,
        box10=None,
        box11=None,
        box13=None,
        box14=None,
        name=None,
        federal_tax_id_type=None,
        city=None,
        zip=None,
        state=None,
        email=None,
        street_address=None,
        tax_id=None,
        contact_id=None,
    ):  # noqa: E501
        """TenNinteyNineContact - a model defined in OpenAPI"""  # noqa: E501

        self._box1 = None
        self._box2 = None
        self._box3 = None
        self._box4 = None
        self._box5 = None
        self._box6 = None
        self._box7 = None
        self._box8 = None
        self._box9 = None
        self._box10 = None
        self._box11 = None
        self._box13 = None
        self._box14 = None
        self._name = None
        self._federal_tax_id_type = None
        self._city = None
        self._zip = None
        self._state = None
        self._email = None
        self._street_address = None
        self._tax_id = None
        self._contact_id = None
        self.discriminator = None

        if box1 is not None:
            self.box1 = box1
        if box2 is not None:
            self.box2 = box2
        if box3 is not None:
            self.box3 = box3
        if box4 is not None:
            self.box4 = box4
        if box5 is not None:
            self.box5 = box5
        if box6 is not None:
            self.box6 = box6
        if box7 is not None:
            self.box7 = box7
        if box8 is not None:
            self.box8 = box8
        if box9 is not None:
            self.box9 = box9
        if box10 is not None:
            self.box10 = box10
        if box11 is not None:
            self.box11 = box11
        if box13 is not None:
            self.box13 = box13
        if box14 is not None:
            self.box14 = box14
        if name is not None:
            self.name = name
        if federal_tax_id_type is not None:
            self.federal_tax_id_type = federal_tax_id_type
        if city is not None:
            self.city = city
        if zip is not None:
            self.zip = zip
        if state is not None:
            self.state = state
        if email is not None:
            self.email = email
        if street_address is not None:
            self.street_address = street_address
        if tax_id is not None:
            self.tax_id = tax_id
        if contact_id is not None:
            self.contact_id = contact_id

    @property
    def box1(self):
        """Gets the box1 of this TenNinteyNineContact.  # noqa: E501

        Box 1 on 1099 Form  # noqa: E501

        :return: The box1 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box1

    @box1.setter
    def box1(self, box1):
        """Sets the box1 of this TenNinteyNineContact.

        Box 1 on 1099 Form  # noqa: E501

        :param box1: The box1 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box1 = box1

    @property
    def box2(self):
        """Gets the box2 of this TenNinteyNineContact.  # noqa: E501

        Box 2 on 1099 Form  # noqa: E501

        :return: The box2 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box2

    @box2.setter
    def box2(self, box2):
        """Sets the box2 of this TenNinteyNineContact.

        Box 2 on 1099 Form  # noqa: E501

        :param box2: The box2 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box2 = box2

    @property
    def box3(self):
        """Gets the box3 of this TenNinteyNineContact.  # noqa: E501

        Box 3 on 1099 Form  # noqa: E501

        :return: The box3 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box3

    @box3.setter
    def box3(self, box3):
        """Sets the box3 of this TenNinteyNineContact.

        Box 3 on 1099 Form  # noqa: E501

        :param box3: The box3 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box3 = box3

    @property
    def box4(self):
        """Gets the box4 of this TenNinteyNineContact.  # noqa: E501

        Box 4 on 1099 Form  # noqa: E501

        :return: The box4 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box4

    @box4.setter
    def box4(self, box4):
        """Sets the box4 of this TenNinteyNineContact.

        Box 4 on 1099 Form  # noqa: E501

        :param box4: The box4 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box4 = box4

    @property
    def box5(self):
        """Gets the box5 of this TenNinteyNineContact.  # noqa: E501

        Box 5 on 1099 Form  # noqa: E501

        :return: The box5 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box5

    @box5.setter
    def box5(self, box5):
        """Sets the box5 of this TenNinteyNineContact.

        Box 5 on 1099 Form  # noqa: E501

        :param box5: The box5 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box5 = box5

    @property
    def box6(self):
        """Gets the box6 of this TenNinteyNineContact.  # noqa: E501

        Box 6 on 1099 Form  # noqa: E501

        :return: The box6 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box6

    @box6.setter
    def box6(self, box6):
        """Sets the box6 of this TenNinteyNineContact.

        Box 6 on 1099 Form  # noqa: E501

        :param box6: The box6 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box6 = box6

    @property
    def box7(self):
        """Gets the box7 of this TenNinteyNineContact.  # noqa: E501

        Box 7 on 1099 Form  # noqa: E501

        :return: The box7 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box7

    @box7.setter
    def box7(self, box7):
        """Sets the box7 of this TenNinteyNineContact.

        Box 7 on 1099 Form  # noqa: E501

        :param box7: The box7 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box7 = box7

    @property
    def box8(self):
        """Gets the box8 of this TenNinteyNineContact.  # noqa: E501

        Box 8 on 1099 Form  # noqa: E501

        :return: The box8 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box8

    @box8.setter
    def box8(self, box8):
        """Sets the box8 of this TenNinteyNineContact.

        Box 8 on 1099 Form  # noqa: E501

        :param box8: The box8 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box8 = box8

    @property
    def box9(self):
        """Gets the box9 of this TenNinteyNineContact.  # noqa: E501

        Box 9 on 1099 Form  # noqa: E501

        :return: The box9 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box9

    @box9.setter
    def box9(self, box9):
        """Sets the box9 of this TenNinteyNineContact.

        Box 9 on 1099 Form  # noqa: E501

        :param box9: The box9 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box9 = box9

    @property
    def box10(self):
        """Gets the box10 of this TenNinteyNineContact.  # noqa: E501

        Box 10 on 1099 Form  # noqa: E501

        :return: The box10 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box10

    @box10.setter
    def box10(self, box10):
        """Sets the box10 of this TenNinteyNineContact.

        Box 10 on 1099 Form  # noqa: E501

        :param box10: The box10 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box10 = box10

    @property
    def box11(self):
        """Gets the box11 of this TenNinteyNineContact.  # noqa: E501

        Box 11 on 1099 Form  # noqa: E501

        :return: The box11 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box11

    @box11.setter
    def box11(self, box11):
        """Sets the box11 of this TenNinteyNineContact.

        Box 11 on 1099 Form  # noqa: E501

        :param box11: The box11 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box11 = box11

    @property
    def box13(self):
        """Gets the box13 of this TenNinteyNineContact.  # noqa: E501

        Box 13 on 1099 Form  # noqa: E501

        :return: The box13 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box13

    @box13.setter
    def box13(self, box13):
        """Sets the box13 of this TenNinteyNineContact.

        Box 13 on 1099 Form  # noqa: E501

        :param box13: The box13 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box13 = box13

    @property
    def box14(self):
        """Gets the box14 of this TenNinteyNineContact.  # noqa: E501

        Box 14 on 1099 Form  # noqa: E501

        :return: The box14 of this TenNinteyNineContact.  # noqa: E501
        :rtype: float
        """
        return self._box14

    @box14.setter
    def box14(self, box14):
        """Sets the box14 of this TenNinteyNineContact.

        Box 14 on 1099 Form  # noqa: E501

        :param box14: The box14 of this TenNinteyNineContact.  # noqa: E501
        :type: float
        """

        self._box14 = box14

    @property
    def name(self):
        """Gets the name of this TenNinteyNineContact.  # noqa: E501

        Contact name on 1099 Form  # noqa: E501

        :return: The name of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenNinteyNineContact.

        Contact name on 1099 Form  # noqa: E501

        :param name: The name of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def federal_tax_id_type(self):
        """Gets the federal_tax_id_type of this TenNinteyNineContact.  # noqa: E501

        Contact Fed Tax ID type  # noqa: E501

        :return: The federal_tax_id_type of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._federal_tax_id_type

    @federal_tax_id_type.setter
    def federal_tax_id_type(self, federal_tax_id_type):
        """Sets the federal_tax_id_type of this TenNinteyNineContact.

        Contact Fed Tax ID type  # noqa: E501

        :param federal_tax_id_type: The federal_tax_id_type of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._federal_tax_id_type = federal_tax_id_type

    @property
    def city(self):
        """Gets the city of this TenNinteyNineContact.  # noqa: E501

        Contact city on 1099 Form  # noqa: E501

        :return: The city of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this TenNinteyNineContact.

        Contact city on 1099 Form  # noqa: E501

        :param city: The city of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def zip(self):
        """Gets the zip of this TenNinteyNineContact.  # noqa: E501

        Contact zip on 1099 Form  # noqa: E501

        :return: The zip of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this TenNinteyNineContact.

        Contact zip on 1099 Form  # noqa: E501

        :param zip: The zip of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def state(self):
        """Gets the state of this TenNinteyNineContact.  # noqa: E501

        Contact State on 1099 Form  # noqa: E501

        :return: The state of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TenNinteyNineContact.

        Contact State on 1099 Form  # noqa: E501

        :param state: The state of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def email(self):
        """Gets the email of this TenNinteyNineContact.  # noqa: E501

        Contact email on 1099 Form  # noqa: E501

        :return: The email of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TenNinteyNineContact.

        Contact email on 1099 Form  # noqa: E501

        :param email: The email of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def street_address(self):
        """Gets the street_address of this TenNinteyNineContact.  # noqa: E501

        Contact address on 1099 Form  # noqa: E501

        :return: The street_address of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this TenNinteyNineContact.

        Contact address on 1099 Form  # noqa: E501

        :param street_address: The street_address of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def tax_id(self):
        """Gets the tax_id of this TenNinteyNineContact.  # noqa: E501

        Contact tax id on 1099 Form  # noqa: E501

        :return: The tax_id of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """Sets the tax_id of this TenNinteyNineContact.

        Contact tax id on 1099 Form  # noqa: E501

        :param tax_id: The tax_id of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._tax_id = tax_id

    @property
    def contact_id(self):
        """Gets the contact_id of this TenNinteyNineContact.  # noqa: E501

        Contact contact id  # noqa: E501

        :return: The contact_id of this TenNinteyNineContact.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this TenNinteyNineContact.

        Contact contact id  # noqa: E501

        :param contact_id: The contact_id of this TenNinteyNineContact.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id
