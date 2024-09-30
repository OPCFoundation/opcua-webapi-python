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

class DeleteSubscriptionsResponse(BaseModel):
    """
    DeleteSubscriptionsResponse
    """
    response_header: Optional[ResponseHeader] = Field(None, alias="ResponseHeader")
    results: Optional[conlist(conint(strict=True, le=4294967295, ge=0))] = Field(None, alias="Results")
    diagnostic_infos: Optional[conlist(DiagnosticInfo)] = Field(None, alias="DiagnosticInfos")
    __properties = ["ResponseHeader", "Results", "DiagnosticInfos"]

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
    def from_json(cls, json_str: str) -> DeleteSubscriptionsResponse:
        """Create an instance of DeleteSubscriptionsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in diagnostic_infos (list)
        _items = []
        if self.diagnostic_infos:
            for _item in self.diagnostic_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['DiagnosticInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeleteSubscriptionsResponse:
        """Create an instance of DeleteSubscriptionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeleteSubscriptionsResponse.parse_obj(obj)

        _obj = DeleteSubscriptionsResponse.parse_obj({
            "response_header": ResponseHeader.from_dict(obj.get("ResponseHeader")) if obj.get("ResponseHeader") is not None else None,
            "results": obj.get("Results"),
            "diagnostic_infos": [DiagnosticInfo.from_dict(_item) for _item in obj.get("DiagnosticInfos")] if obj.get("DiagnosticInfos") is not None else None
        })
        return _obj


