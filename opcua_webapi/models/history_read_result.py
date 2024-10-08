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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBytes, StrictStr, conint
from opcua_webapi.models.extension_object import ExtensionObject

class HistoryReadResult(BaseModel):
    """
    HistoryReadResult
    """
    status_code: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="StatusCode")
    continuation_point: Optional[Union[StrictBytes, StrictStr]] = Field(None, alias="ContinuationPoint")
    history_data: Optional[ExtensionObject] = Field(None, alias="HistoryData")
    __properties = ["StatusCode", "ContinuationPoint", "HistoryData"]

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
    def from_json(cls, json_str: str) -> HistoryReadResult:
        """Create an instance of HistoryReadResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of history_data
        if self.history_data:
            _dict['HistoryData'] = self.history_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HistoryReadResult:
        """Create an instance of HistoryReadResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HistoryReadResult.parse_obj(obj)

        _obj = HistoryReadResult.parse_obj({
            "status_code": obj.get("StatusCode"),
            "continuation_point": obj.get("ContinuationPoint"),
            "history_data": ExtensionObject.from_dict(obj.get("HistoryData")) if obj.get("HistoryData") is not None else None
        })
        return _obj


