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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.browse_result import BrowseResult
from opcua_webapi.models.diagnostic_info import DiagnosticInfo
from opcua_webapi.models.response_header import ResponseHeader
from typing import Optional, Set
from typing_extensions import Self

class BrowseResponse(BaseModel):
    """
    BrowseResponse
    """ # noqa: E501
    response_header: Optional[ResponseHeader] = Field(default=None, alias="ResponseHeader")
    results: Optional[List[BrowseResult]] = Field(default=None, alias="Results")
    diagnostic_infos: Optional[List[DiagnosticInfo]] = Field(default=None, alias="DiagnosticInfos")
    __properties: ClassVar[List[str]] = ["ResponseHeader", "Results", "DiagnosticInfos"]

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
        """Create an instance of BrowseResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response_header
        if self.response_header:
            _dict['ResponseHeader'] = self.response_header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['Results'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in diagnostic_infos (list)
        _items = []
        if self.diagnostic_infos:
            for _item_diagnostic_infos in self.diagnostic_infos:
                if _item_diagnostic_infos:
                    _items.append(_item_diagnostic_infos.to_dict())
            _dict['DiagnosticInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BrowseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ResponseHeader": ResponseHeader.from_dict(obj["ResponseHeader"]) if obj.get("ResponseHeader") is not None else None,
            "Results": [BrowseResult.from_dict(_item) for _item in obj["Results"]] if obj.get("Results") is not None else None,
            "DiagnosticInfos": [DiagnosticInfo.from_dict(_item) for _item in obj["DiagnosticInfos"]] if obj.get("DiagnosticInfos") is not None else None
        })
        return _obj


