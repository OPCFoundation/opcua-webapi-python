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
from pydantic import BaseModel, Field, StrictBytes, StrictStr

class UserNameIdentityToken(BaseModel):
    """
    UserNameIdentityToken
    """
    user_name: Optional[StrictStr] = Field(None, alias="UserName")
    password: Optional[Union[StrictBytes, StrictStr]] = Field(None, alias="Password")
    encryption_algorithm: Optional[StrictStr] = Field(None, alias="EncryptionAlgorithm")
    policy_id: Optional[StrictStr] = Field(None, alias="PolicyId")
    __properties = ["PolicyId"]

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
    def from_json(cls, json_str: str) -> UserNameIdentityToken:
        """Create an instance of UserNameIdentityToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserNameIdentityToken:
        """Create an instance of UserNameIdentityToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserNameIdentityToken.parse_obj(obj)

        _obj = UserNameIdentityToken.parse_obj({
            "policy_id": obj.get("PolicyId")
        })
        return _obj


