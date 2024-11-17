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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class JsonActionNetworkMessage(BaseModel):
    """
    JsonActionNetworkMessage
    """ # noqa: E501
    message_id: Optional[StrictStr] = Field(default=None, alias="MessageId")
    message_type: Optional[StrictStr] = Field(default=None, alias="MessageType")
    publisher_id: Optional[StrictStr] = Field(default=None, alias="PublisherId")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    response_address: Optional[StrictStr] = Field(default=None, alias="ResponseAddress")
    correlation_data: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, alias="CorrelationData")
    requestor_id: Optional[StrictStr] = Field(default=None, alias="RequestorId")
    timeout_hint: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="TimeoutHint")
    messages: Optional[List[Dict[str, Any]]] = Field(default=None, alias="Messages")
    __properties: ClassVar[List[str]] = ["MessageId", "MessageType", "PublisherId", "Timestamp", "ResponseAddress", "CorrelationData", "RequestorId", "TimeoutHint", "Messages"]

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
        """Create an instance of JsonActionNetworkMessage from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JsonActionNetworkMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MessageId": obj.get("MessageId"),
            "MessageType": obj.get("MessageType"),
            "PublisherId": obj.get("PublisherId"),
            "Timestamp": obj.get("Timestamp"),
            "ResponseAddress": obj.get("ResponseAddress"),
            "CorrelationData": obj.get("CorrelationData"),
            "RequestorId": obj.get("RequestorId"),
            "TimeoutHint": obj.get("TimeoutHint") if obj.get("TimeoutHint") is not None else 0,
            "Messages": obj.get("Messages")
        })
        return _obj

