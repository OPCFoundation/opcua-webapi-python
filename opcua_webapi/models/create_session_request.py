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
from pydantic import BaseModel, Field, StrictBytes, StrictFloat, StrictInt, StrictStr, conint
from opcua_webapi.models.application_description import ApplicationDescription
from opcua_webapi.models.request_header import RequestHeader

class CreateSessionRequest(BaseModel):
    """
    CreateSessionRequest
    """
    request_header: Optional[RequestHeader] = Field(None, alias="RequestHeader")
    client_description: Optional[ApplicationDescription] = Field(None, alias="ClientDescription")
    server_uri: Optional[StrictStr] = Field(None, alias="ServerUri")
    endpoint_url: Optional[StrictStr] = Field(None, alias="EndpointUrl")
    session_name: Optional[StrictStr] = Field(None, alias="SessionName")
    client_nonce: Optional[Union[StrictBytes, StrictStr]] = Field(None, alias="ClientNonce")
    client_certificate: Optional[Union[StrictBytes, StrictStr]] = Field(None, alias="ClientCertificate")
    requested_session_timeout: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="RequestedSessionTimeout")
    max_response_message_size: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="MaxResponseMessageSize")
    __properties = ["RequestHeader", "ClientDescription", "ServerUri", "EndpointUrl", "SessionName", "ClientNonce", "ClientCertificate", "RequestedSessionTimeout", "MaxResponseMessageSize"]

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
    def from_json(cls, json_str: str) -> CreateSessionRequest:
        """Create an instance of CreateSessionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_description
        if self.client_description:
            _dict['ClientDescription'] = self.client_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSessionRequest:
        """Create an instance of CreateSessionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSessionRequest.parse_obj(obj)

        _obj = CreateSessionRequest.parse_obj({
            "request_header": RequestHeader.from_dict(obj.get("RequestHeader")) if obj.get("RequestHeader") is not None else None,
            "client_description": ApplicationDescription.from_dict(obj.get("ClientDescription")) if obj.get("ClientDescription") is not None else None,
            "server_uri": obj.get("ServerUri"),
            "endpoint_url": obj.get("EndpointUrl"),
            "session_name": obj.get("SessionName"),
            "client_nonce": obj.get("ClientNonce"),
            "client_certificate": obj.get("ClientCertificate"),
            "requested_session_timeout": obj.get("RequestedSessionTimeout"),
            "max_response_message_size": obj.get("MaxResponseMessageSize")
        })
        return _obj


