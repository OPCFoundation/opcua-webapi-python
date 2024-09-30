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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, conint, conlist
from opcua_webapi.models.extension_object import ExtensionObject

class NotificationMessage(BaseModel):
    """
    NotificationMessage
    """
    sequence_number: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="SequenceNumber")
    publish_time: Optional[datetime] = Field(None, alias="PublishTime")
    notification_data: Optional[conlist(ExtensionObject)] = Field(None, alias="NotificationData")
    __properties = ["SequenceNumber", "PublishTime", "NotificationData"]

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
    def from_json(cls, json_str: str) -> NotificationMessage:
        """Create an instance of NotificationMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notification_data (list)
        _items = []
        if self.notification_data:
            for _item in self.notification_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['NotificationData'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationMessage:
        """Create an instance of NotificationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotificationMessage.parse_obj(obj)

        _obj = NotificationMessage.parse_obj({
            "sequence_number": obj.get("SequenceNumber"),
            "publish_time": obj.get("PublishTime"),
            "notification_data": [ExtensionObject.from_dict(_item) for _item in obj.get("NotificationData")] if obj.get("NotificationData") is not None else None
        })
        return _obj


