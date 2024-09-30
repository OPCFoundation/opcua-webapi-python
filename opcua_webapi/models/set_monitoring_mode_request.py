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
from pydantic import BaseModel, Field, StrictInt, conint, conlist
from opcua_webapi.models.request_header import RequestHeader

class SetMonitoringModeRequest(BaseModel):
    """
    SetMonitoringModeRequest
    """
    request_header: Optional[RequestHeader] = Field(None, alias="RequestHeader")
    subscription_id: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="SubscriptionId")
    monitoring_mode: Optional[StrictInt] = Field(None, alias="MonitoringMode")
    monitored_item_ids: Optional[conlist(conint(strict=True, le=4294967295, ge=0))] = Field(None, alias="MonitoredItemIds")
    __properties = ["RequestHeader", "SubscriptionId", "MonitoringMode", "MonitoredItemIds"]

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
    def from_json(cls, json_str: str) -> SetMonitoringModeRequest:
        """Create an instance of SetMonitoringModeRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetMonitoringModeRequest:
        """Create an instance of SetMonitoringModeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetMonitoringModeRequest.parse_obj(obj)

        _obj = SetMonitoringModeRequest.parse_obj({
            "request_header": RequestHeader.from_dict(obj.get("RequestHeader")) if obj.get("RequestHeader") is not None else None,
            "subscription_id": obj.get("SubscriptionId"),
            "monitoring_mode": obj.get("MonitoringMode"),
            "monitored_item_ids": obj.get("MonitoredItemIds")
        })
        return _obj


