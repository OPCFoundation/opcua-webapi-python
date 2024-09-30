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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from opcua_webapi.models.structure_definition import StructureDefinition

class StructureDescription(BaseModel):
    """
    StructureDescription
    """
    structure_definition: Optional[StructureDefinition] = Field(None, alias="StructureDefinition")
    data_type_id: Optional[StrictStr] = Field(None, alias="DataTypeId")
    name: Optional[StrictStr] = Field(None, alias="Name")
    __properties = ["DataTypeId", "Name"]

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
    def from_json(cls, json_str: str) -> StructureDescription:
        """Create an instance of StructureDescription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StructureDescription:
        """Create an instance of StructureDescription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StructureDescription.parse_obj(obj)

        _obj = StructureDescription.parse_obj({
            "data_type_id": obj.get("DataTypeId"),
            "name": obj.get("Name")
        })
        return _obj


