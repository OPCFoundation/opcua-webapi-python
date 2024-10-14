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
from typing_extensions import Annotated
from opcua_webapi.models.diagnostic_info import DiagnosticInfo
from typing import Optional, Set
from typing_extensions import Self

class ContentFilterElementResult(BaseModel):
    """
    ContentFilterElementResult
    """ # noqa: E501
    status_code: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=None, alias="StatusCode")
    operand_status_codes: Optional[List[Annotated[int, Field(le=4294967295, strict=True, ge=0)]]] = Field(default=None, alias="OperandStatusCodes")
    operand_diagnostic_infos: Optional[List[DiagnosticInfo]] = Field(default=None, alias="OperandDiagnosticInfos")
    __properties: ClassVar[List[str]] = ["StatusCode", "OperandStatusCodes", "OperandDiagnosticInfos"]

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
        """Create an instance of ContentFilterElementResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in operand_diagnostic_infos (list)
        _items = []
        if self.operand_diagnostic_infos:
            for _item_operand_diagnostic_infos in self.operand_diagnostic_infos:
                if _item_operand_diagnostic_infos:
                    _items.append(_item_operand_diagnostic_infos.to_dict())
            _dict['OperandDiagnosticInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentFilterElementResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "StatusCode": obj.get("StatusCode"),
            "OperandStatusCodes": obj.get("OperandStatusCodes"),
            "OperandDiagnosticInfos": [DiagnosticInfo.from_dict(_item) for _item in obj["OperandDiagnosticInfos"]] if obj.get("OperandDiagnosticInfos") is not None else None
        })
        return _obj

