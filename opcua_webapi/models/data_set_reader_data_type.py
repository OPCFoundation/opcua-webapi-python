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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from opcua_webapi.models.data_set_meta_data_type import DataSetMetaDataType
from opcua_webapi.models.endpoint_description import EndpointDescription
from opcua_webapi.models.extension_object import ExtensionObject
from opcua_webapi.models.key_value_pair import KeyValuePair
from opcua_webapi.models.variant import Variant
from typing import Optional, Set
from typing_extensions import Self

class DataSetReaderDataType(BaseModel):
    """
    DataSetReaderDataType
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    enabled: Optional[StrictBool] = Field(default=None, alias="Enabled")
    publisher_id: Optional[Variant] = Field(default=None, alias="PublisherId")
    writer_group_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, alias="WriterGroupId")
    data_set_writer_id: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, alias="DataSetWriterId")
    data_set_meta_data: Optional[DataSetMetaDataType] = Field(default=None, alias="DataSetMetaData")
    data_set_field_content_mask: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=None, alias="DataSetFieldContentMask")
    message_receive_timeout: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="MessageReceiveTimeout")
    key_frame_count: Optional[Annotated[int, Field(le=4294967295, strict=True, ge=0)]] = Field(default=None, alias="KeyFrameCount")
    header_layout_uri: Optional[StrictStr] = Field(default=None, alias="HeaderLayoutUri")
    security_mode: Optional[StrictInt] = Field(default=None, alias="SecurityMode")
    security_group_id: Optional[StrictStr] = Field(default=None, alias="SecurityGroupId")
    security_key_services: Optional[List[EndpointDescription]] = Field(default=None, alias="SecurityKeyServices")
    data_set_reader_properties: Optional[List[KeyValuePair]] = Field(default=None, alias="DataSetReaderProperties")
    transport_settings: Optional[ExtensionObject] = Field(default=None, alias="TransportSettings")
    message_settings: Optional[ExtensionObject] = Field(default=None, alias="MessageSettings")
    subscribed_data_set: Optional[ExtensionObject] = Field(default=None, alias="SubscribedDataSet")
    __properties: ClassVar[List[str]] = ["Name", "Enabled", "PublisherId", "WriterGroupId", "DataSetWriterId", "DataSetMetaData", "DataSetFieldContentMask", "MessageReceiveTimeout", "KeyFrameCount", "HeaderLayoutUri", "SecurityMode", "SecurityGroupId", "SecurityKeyServices", "DataSetReaderProperties", "TransportSettings", "MessageSettings", "SubscribedDataSet"]

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
        """Create an instance of DataSetReaderDataType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of publisher_id
        if self.publisher_id:
            _dict['PublisherId'] = self.publisher_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_set_meta_data
        if self.data_set_meta_data:
            _dict['DataSetMetaData'] = self.data_set_meta_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in security_key_services (list)
        _items = []
        if self.security_key_services:
            for _item_security_key_services in self.security_key_services:
                if _item_security_key_services:
                    _items.append(_item_security_key_services.to_dict())
            _dict['SecurityKeyServices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_set_reader_properties (list)
        _items = []
        if self.data_set_reader_properties:
            for _item_data_set_reader_properties in self.data_set_reader_properties:
                if _item_data_set_reader_properties:
                    _items.append(_item_data_set_reader_properties.to_dict())
            _dict['DataSetReaderProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of transport_settings
        if self.transport_settings:
            _dict['TransportSettings'] = self.transport_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message_settings
        if self.message_settings:
            _dict['MessageSettings'] = self.message_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscribed_data_set
        if self.subscribed_data_set:
            _dict['SubscribedDataSet'] = self.subscribed_data_set.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataSetReaderDataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Enabled": obj.get("Enabled"),
            "PublisherId": Variant.from_dict(obj["PublisherId"]) if obj.get("PublisherId") is not None else None,
            "WriterGroupId": obj.get("WriterGroupId"),
            "DataSetWriterId": obj.get("DataSetWriterId"),
            "DataSetMetaData": DataSetMetaDataType.from_dict(obj["DataSetMetaData"]) if obj.get("DataSetMetaData") is not None else None,
            "DataSetFieldContentMask": obj.get("DataSetFieldContentMask"),
            "MessageReceiveTimeout": obj.get("MessageReceiveTimeout"),
            "KeyFrameCount": obj.get("KeyFrameCount"),
            "HeaderLayoutUri": obj.get("HeaderLayoutUri"),
            "SecurityMode": obj.get("SecurityMode"),
            "SecurityGroupId": obj.get("SecurityGroupId"),
            "SecurityKeyServices": [EndpointDescription.from_dict(_item) for _item in obj["SecurityKeyServices"]] if obj.get("SecurityKeyServices") is not None else None,
            "DataSetReaderProperties": [KeyValuePair.from_dict(_item) for _item in obj["DataSetReaderProperties"]] if obj.get("DataSetReaderProperties") is not None else None,
            "TransportSettings": ExtensionObject.from_dict(obj["TransportSettings"]) if obj.get("TransportSettings") is not None else None,
            "MessageSettings": ExtensionObject.from_dict(obj["MessageSettings"]) if obj.get("MessageSettings") is not None else None,
            "SubscribedDataSet": ExtensionObject.from_dict(obj["SubscribedDataSet"]) if obj.get("SubscribedDataSet") is not None else None
        })
        return _obj

