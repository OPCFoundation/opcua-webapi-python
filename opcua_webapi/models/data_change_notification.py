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
from opcua_webapi.models.diagnostic_info import DiagnosticInfo
from opcua_webapi.models.monitored_item_notification import MonitoredItemNotification

class DataChangeNotification(BaseModel):
    """
    DataChangeNotification
    """
    monitored_items: Optional[conlist(MonitoredItemNotification)] = Field(None, alias="MonitoredItems")
    diagnostic_infos: Optional[conlist(DiagnosticInfo)] = Field(None, alias="DiagnosticInfos")
    __properties = []

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
    def from_json(cls, json_str: str) -> DataChangeNotification:
        """Create an instance of DataChangeNotification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataChangeNotification:
        """Create an instance of DataChangeNotification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataChangeNotification.parse_obj(obj)

        _obj = DataChangeNotification.parse_obj({
        })
        return _obj


