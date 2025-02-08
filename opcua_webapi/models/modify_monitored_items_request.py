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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from opcua_webapi.models.monitored_item_modify_request import MonitoredItemModifyRequest
from opcua_webapi.models.request_header import RequestHeader
from typing import Optional, Set
from typing_extensions import Self

class ModifyMonitoredItemsRequest(BaseModel):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.3/#5.13.3.2).
    """ # noqa: E501
    request_header: Optional[RequestHeader] = Field(default=None, alias="RequestHeader")
    subscription_id: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=0, alias="SubscriptionId")
    timestamps_to_return: Optional[StrictInt] = Field(default=None, description="[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.40).", alias="TimestampsToReturn")
    items_to_modify: Optional[List[MonitoredItemModifyRequest]] = Field(default=None, alias="ItemsToModify")
    __properties: ClassVar[List[str]] = ["RequestHeader", "SubscriptionId", "TimestampsToReturn", "ItemsToModify"]

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
        """Create an instance of ModifyMonitoredItemsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items_to_modify (list)
        _items = []
        if self.items_to_modify:
            for _item_items_to_modify in self.items_to_modify:
                if _item_items_to_modify:
                    _items.append(_item_items_to_modify.to_dict())
            _dict['ItemsToModify'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModifyMonitoredItemsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RequestHeader": RequestHeader.from_dict(obj["RequestHeader"]) if obj.get("RequestHeader") is not None else None,
            "SubscriptionId": obj.get("SubscriptionId") if obj.get("SubscriptionId") is not None else 0,
            "TimestampsToReturn": obj.get("TimestampsToReturn"),
            "ItemsToModify": [MonitoredItemModifyRequest.from_dict(_item) for _item in obj["ItemsToModify"]] if obj.get("ItemsToModify") is not None else None
        })
        return _obj


