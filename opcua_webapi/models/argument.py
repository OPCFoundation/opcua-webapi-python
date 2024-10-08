# coding: utf-8

"""
    OPC UA Web API

    This API provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist
from opcua_webapi.models.localized_text import LocalizedText

class Argument(BaseModel):
    """
    Argument
    """
    name: Optional[StrictStr] = Field(None, alias="Name")
    data_type: Optional[StrictStr] = Field(None, alias="DataType")
    value_rank: Optional[StrictInt] = Field(None, alias="ValueRank")
    array_dimensions: Optional[conlist(conint(strict=True, le=4294967295, ge=0))] = Field(None, alias="ArrayDimensions")
    description: Optional[LocalizedText] = Field(None, alias="Description")
    __properties = ["Name", "DataType", "ValueRank", "ArrayDimensions", "Description"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Argument:
        """Create an instance of Argument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['Description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Argument:
        """Create an instance of Argument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Argument.parse_obj(obj)

        _obj = Argument.parse_obj({
            "name": obj.get("Name"),
            "data_type": obj.get("DataType"),
            "value_rank": obj.get("ValueRank"),
            "array_dimensions": obj.get("ArrayDimensions"),
            "description": LocalizedText.from_dict(obj.get("Description")) if obj.get("Description") is not None else None
        })
        return _obj


