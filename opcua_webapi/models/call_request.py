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
from pydantic import BaseModel, Field, conlist
from opcua_webapi.models.call_method_request import CallMethodRequest
from opcua_webapi.models.request_header import RequestHeader

class CallRequest(BaseModel):
    """
    CallRequest
    """
    request_header: Optional[RequestHeader] = Field(None, alias="RequestHeader")
    methods_to_call: Optional[conlist(CallMethodRequest)] = Field(None, alias="MethodsToCall")
    __properties = ["RequestHeader", "MethodsToCall"]

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
    def from_json(cls, json_str: str) -> CallRequest:
        """Create an instance of CallRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of request_header
        if self.request_header:
            _dict['RequestHeader'] = self.request_header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in methods_to_call (list)
        _items = []
        if self.methods_to_call:
            for _item in self.methods_to_call:
                if _item:
                    _items.append(_item.to_dict())
            _dict['MethodsToCall'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CallRequest:
        """Create an instance of CallRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CallRequest.parse_obj(obj)

        _obj = CallRequest.parse_obj({
            "request_header": RequestHeader.from_dict(obj.get("RequestHeader")) if obj.get("RequestHeader") is not None else None,
            "methods_to_call": [CallMethodRequest.from_dict(_item) for _item in obj.get("MethodsToCall")] if obj.get("MethodsToCall") is not None else None
        })
        return _obj


