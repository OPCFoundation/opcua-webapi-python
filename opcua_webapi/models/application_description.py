# coding: utf-8

"""
    OPC UA Web API

    Provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.localized_text import LocalizedText
from typing import Optional, Set
from typing_extensions import Self

class ApplicationDescription(BaseModel):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/7.2.4/#7.2.4.6.5).
    """ # noqa: E501
    application_uri: Optional[StrictStr] = Field(default=None, alias="ApplicationUri")
    product_uri: Optional[StrictStr] = Field(default=None, alias="ProductUri")
    application_name: Optional[LocalizedText] = Field(default=None, alias="ApplicationName")
    application_type: Optional[StrictInt] = Field(default=None, description="[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.4).", alias="ApplicationType")
    gateway_server_uri: Optional[StrictStr] = Field(default=None, alias="GatewayServerUri")
    discovery_profile_uri: Optional[StrictStr] = Field(default=None, alias="DiscoveryProfileUri")
    discovery_urls: Optional[List[StrictStr]] = Field(default=None, alias="DiscoveryUrls")
    __properties: ClassVar[List[str]] = ["ApplicationUri", "ProductUri", "ApplicationName", "ApplicationType", "GatewayServerUri", "DiscoveryProfileUri", "DiscoveryUrls"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApplicationDescription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of application_name
        if self.application_name:
            _dict['ApplicationName'] = self.application_name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationDescription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ApplicationUri": obj.get("ApplicationUri"),
            "ProductUri": obj.get("ProductUri"),
            "ApplicationName": LocalizedText.from_dict(obj["ApplicationName"]) if obj.get("ApplicationName") is not None else None,
            "ApplicationType": obj.get("ApplicationType"),
            "GatewayServerUri": obj.get("GatewayServerUri"),
            "DiscoveryProfileUri": obj.get("DiscoveryProfileUri"),
            "DiscoveryUrls": obj.get("DiscoveryUrls")
        })
        return _obj


