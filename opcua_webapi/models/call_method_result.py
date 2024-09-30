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
from pydantic import BaseModel, Field, conint, conlist
from opcua_webapi.models.diagnostic_info import DiagnosticInfo
from opcua_webapi.models.variant import Variant

class CallMethodResult(BaseModel):
    """
    CallMethodResult
    """
    status_code: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="StatusCode")
    input_argument_results: Optional[conlist(conint(strict=True, le=4294967295, ge=0))] = Field(None, alias="InputArgumentResults")
    input_argument_diagnostic_infos: Optional[conlist(DiagnosticInfo)] = Field(None, alias="InputArgumentDiagnosticInfos")
    output_arguments: Optional[conlist(Variant)] = Field(None, alias="OutputArguments")
    __properties = ["StatusCode", "InputArgumentResults", "InputArgumentDiagnosticInfos", "OutputArguments"]

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
    def from_json(cls, json_str: str) -> CallMethodResult:
        """Create an instance of CallMethodResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in input_argument_diagnostic_infos (list)
        _items = []
        if self.input_argument_diagnostic_infos:
            for _item in self.input_argument_diagnostic_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['InputArgumentDiagnosticInfos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in output_arguments (list)
        _items = []
        if self.output_arguments:
            for _item in self.output_arguments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['OutputArguments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CallMethodResult:
        """Create an instance of CallMethodResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CallMethodResult.parse_obj(obj)

        _obj = CallMethodResult.parse_obj({
            "status_code": obj.get("StatusCode"),
            "input_argument_results": obj.get("InputArgumentResults"),
            "input_argument_diagnostic_infos": [DiagnosticInfo.from_dict(_item) for _item in obj.get("InputArgumentDiagnosticInfos")] if obj.get("InputArgumentDiagnosticInfos") is not None else None,
            "output_arguments": [Variant.from_dict(_item) for _item in obj.get("OutputArguments")] if obj.get("OutputArguments") is not None else None
        })
        return _obj


