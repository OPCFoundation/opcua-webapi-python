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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.extension_object import ExtensionObject
from opcua_webapi.models.request_header import RequestHeader
from opcua_webapi.models.signature_data import SignatureData
from opcua_webapi.models.signed_software_certificate import SignedSoftwareCertificate
from typing import Optional, Set
from typing_extensions import Self

class ActivateSessionRequest(BaseModel):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.3/#5.7.3.2).
    """ # noqa: E501
    request_header: Optional[RequestHeader] = Field(default=None, alias="RequestHeader")
    client_signature: Optional[SignatureData] = Field(default=None, alias="ClientSignature")
    client_software_certificates: Optional[List[SignedSoftwareCertificate]] = Field(default=None, alias="ClientSoftwareCertificates")
    locale_ids: Optional[List[StrictStr]] = Field(default=None, alias="LocaleIds")
    user_identity_token: Optional[ExtensionObject] = Field(default=None, alias="UserIdentityToken")
    user_token_signature: Optional[SignatureData] = Field(default=None, alias="UserTokenSignature")
    __properties: ClassVar[List[str]] = ["RequestHeader", "ClientSignature", "ClientSoftwareCertificates", "LocaleIds", "UserIdentityToken", "UserTokenSignature"]

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
        """Create an instance of ActivateSessionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of request_header
        if self.request_header:
            _dict['RequestHeader'] = self.request_header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_signature
        if self.client_signature:
            _dict['ClientSignature'] = self.client_signature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in client_software_certificates (list)
        _items = []
        if self.client_software_certificates:
            for _item_client_software_certificates in self.client_software_certificates:
                if _item_client_software_certificates:
                    _items.append(_item_client_software_certificates.to_dict())
            _dict['ClientSoftwareCertificates'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_identity_token
        if self.user_identity_token:
            _dict['UserIdentityToken'] = self.user_identity_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_token_signature
        if self.user_token_signature:
            _dict['UserTokenSignature'] = self.user_token_signature.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActivateSessionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RequestHeader": RequestHeader.from_dict(obj["RequestHeader"]) if obj.get("RequestHeader") is not None else None,
            "ClientSignature": SignatureData.from_dict(obj["ClientSignature"]) if obj.get("ClientSignature") is not None else None,
            "ClientSoftwareCertificates": [SignedSoftwareCertificate.from_dict(_item) for _item in obj["ClientSoftwareCertificates"]] if obj.get("ClientSoftwareCertificates") is not None else None,
            "LocaleIds": obj.get("LocaleIds"),
            "UserIdentityToken": ExtensionObject.from_dict(obj["UserIdentityToken"]) if obj.get("UserIdentityToken") is not None else None,
            "UserTokenSignature": SignatureData.from_dict(obj["UserTokenSignature"]) if obj.get("UserTokenSignature") is not None else None
        })
        return _obj


