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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class LocalizedText(BaseModel):
    """
    LocalizedText
    """
    locale: Optional[StrictStr] = Field(None, alias="Locale")
    text: Optional[StrictStr] = Field(None, alias="Text")
    __properties = ["Locale", "Text"]

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
    def from_json(cls, json_str: str) -> LocalizedText:
        """Create an instance of LocalizedText from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocalizedText:
        """Create an instance of LocalizedText from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocalizedText.parse_obj(obj)

        _obj = LocalizedText.parse_obj({
            "locale": obj.get("Locale"),
            "text": obj.get("Text")
        })
        return _obj


