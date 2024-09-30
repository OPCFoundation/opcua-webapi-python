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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, conint
from opcua_webapi.models.extension_object import ExtensionObject

class MonitoringParameters(BaseModel):
    """
    MonitoringParameters
    """
    client_handle: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="ClientHandle")
    sampling_interval: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="SamplingInterval")
    filter: Optional[ExtensionObject] = Field(None, alias="Filter")
    queue_size: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="QueueSize")
    discard_oldest: Optional[StrictBool] = Field(None, alias="DiscardOldest")
    __properties = ["ClientHandle", "SamplingInterval", "Filter", "QueueSize", "DiscardOldest"]

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
    def from_json(cls, json_str: str) -> MonitoringParameters:
        """Create an instance of MonitoringParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['Filter'] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MonitoringParameters:
        """Create an instance of MonitoringParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MonitoringParameters.parse_obj(obj)

        _obj = MonitoringParameters.parse_obj({
            "client_handle": obj.get("ClientHandle"),
            "sampling_interval": obj.get("SamplingInterval"),
            "filter": ExtensionObject.from_dict(obj.get("Filter")) if obj.get("Filter") is not None else None,
            "queue_size": obj.get("QueueSize"),
            "discard_oldest": obj.get("DiscardOldest")
        })
        return _obj


