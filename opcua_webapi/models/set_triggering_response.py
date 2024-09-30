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
from opcua_webapi.models.response_header import ResponseHeader

class SetTriggeringResponse(BaseModel):
    """
    SetTriggeringResponse
    """
    response_header: Optional[ResponseHeader] = Field(None, alias="ResponseHeader")
    add_results: Optional[conlist(conint(strict=True, le=4294967295, ge=0))] = Field(None, alias="AddResults")
    add_diagnostic_infos: Optional[conlist(DiagnosticInfo)] = Field(None, alias="AddDiagnosticInfos")
    remove_results: Optional[conlist(conint(strict=True, le=4294967295, ge=0))] = Field(None, alias="RemoveResults")
    remove_diagnostic_infos: Optional[conlist(DiagnosticInfo)] = Field(None, alias="RemoveDiagnosticInfos")
    __properties = ["ResponseHeader", "AddResults", "AddDiagnosticInfos", "RemoveResults", "RemoveDiagnosticInfos"]

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
    def from_json(cls, json_str: str) -> SetTriggeringResponse:
        """Create an instance of SetTriggeringResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of response_header
        if self.response_header:
            _dict['ResponseHeader'] = self.response_header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in add_diagnostic_infos (list)
        _items = []
        if self.add_diagnostic_infos:
            for _item in self.add_diagnostic_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AddDiagnosticInfos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in remove_diagnostic_infos (list)
        _items = []
        if self.remove_diagnostic_infos:
            for _item in self.remove_diagnostic_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['RemoveDiagnosticInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetTriggeringResponse:
        """Create an instance of SetTriggeringResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetTriggeringResponse.parse_obj(obj)

        _obj = SetTriggeringResponse.parse_obj({
            "response_header": ResponseHeader.from_dict(obj.get("ResponseHeader")) if obj.get("ResponseHeader") is not None else None,
            "add_results": obj.get("AddResults"),
            "add_diagnostic_infos": [DiagnosticInfo.from_dict(_item) for _item in obj.get("AddDiagnosticInfos")] if obj.get("AddDiagnosticInfos") is not None else None,
            "remove_results": obj.get("RemoveResults"),
            "remove_diagnostic_infos": [DiagnosticInfo.from_dict(_item) for _item in obj.get("RemoveDiagnosticInfos")] if obj.get("RemoveDiagnosticInfos") is not None else None
        })
        return _obj


