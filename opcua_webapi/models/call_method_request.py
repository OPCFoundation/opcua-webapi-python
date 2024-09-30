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
from pydantic import BaseModel, Field, StrictStr, conlist
from opcua_webapi.models.variant import Variant

class CallMethodRequest(BaseModel):
    """
    CallMethodRequest
    """
    object_id: Optional[StrictStr] = Field(None, alias="ObjectId")
    method_id: Optional[StrictStr] = Field(None, alias="MethodId")
    input_arguments: Optional[conlist(Variant)] = Field(None, alias="InputArguments")
    __properties = ["ObjectId", "MethodId", "InputArguments"]

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
    def from_json(cls, json_str: str) -> CallMethodRequest:
        """Create an instance of CallMethodRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in input_arguments (list)
        _items = []
        if self.input_arguments:
            for _item in self.input_arguments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['InputArguments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CallMethodRequest:
        """Create an instance of CallMethodRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CallMethodRequest.parse_obj(obj)

        _obj = CallMethodRequest.parse_obj({
            "object_id": obj.get("ObjectId"),
            "method_id": obj.get("MethodId"),
            "input_arguments": [Variant.from_dict(_item) for _item in obj.get("InputArguments")] if obj.get("InputArguments") is not None else None
        })
        return _obj


