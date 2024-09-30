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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist
from opcua_webapi.models.endpoint_description import EndpointDescription
from opcua_webapi.models.key_value_pair import KeyValuePair

class PubSubGroupDataType(BaseModel):
    """
    PubSubGroupDataType
    """
    name: Optional[StrictStr] = Field(None, alias="Name")
    enabled: Optional[StrictBool] = Field(None, alias="Enabled")
    security_mode: Optional[StrictInt] = Field(None, alias="SecurityMode")
    security_group_id: Optional[StrictStr] = Field(None, alias="SecurityGroupId")
    security_key_services: Optional[conlist(EndpointDescription)] = Field(None, alias="SecurityKeyServices")
    max_network_message_size: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="MaxNetworkMessageSize")
    group_properties: Optional[conlist(KeyValuePair)] = Field(None, alias="GroupProperties")
    __properties = ["Name", "Enabled", "SecurityMode", "SecurityGroupId", "SecurityKeyServices", "MaxNetworkMessageSize", "GroupProperties"]

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
    def from_json(cls, json_str: str) -> PubSubGroupDataType:
        """Create an instance of PubSubGroupDataType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in security_key_services (list)
        _items = []
        if self.security_key_services:
            for _item in self.security_key_services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SecurityKeyServices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in group_properties (list)
        _items = []
        if self.group_properties:
            for _item in self.group_properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['GroupProperties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PubSubGroupDataType:
        """Create an instance of PubSubGroupDataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PubSubGroupDataType.parse_obj(obj)

        _obj = PubSubGroupDataType.parse_obj({
            "name": obj.get("Name"),
            "enabled": obj.get("Enabled"),
            "security_mode": obj.get("SecurityMode"),
            "security_group_id": obj.get("SecurityGroupId"),
            "security_key_services": [EndpointDescription.from_dict(_item) for _item in obj.get("SecurityKeyServices")] if obj.get("SecurityKeyServices") is not None else None,
            "max_network_message_size": obj.get("MaxNetworkMessageSize"),
            "group_properties": [KeyValuePair.from_dict(_item) for _item in obj.get("GroupProperties")] if obj.get("GroupProperties") is not None else None
        })
        return _obj


