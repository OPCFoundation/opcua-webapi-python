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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conint, conlist
from opcua_webapi.models.data_set_meta_data_type import DataSetMetaDataType
from opcua_webapi.models.endpoint_description import EndpointDescription
from opcua_webapi.models.extension_object import ExtensionObject
from opcua_webapi.models.key_value_pair import KeyValuePair
from opcua_webapi.models.variant import Variant

class DataSetReaderDataType(BaseModel):
    """
    DataSetReaderDataType
    """
    name: Optional[StrictStr] = Field(None, alias="Name")
    enabled: Optional[StrictBool] = Field(None, alias="Enabled")
    publisher_id: Optional[Variant] = Field(None, alias="PublisherId")
    writer_group_id: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="WriterGroupId")
    data_set_writer_id: Optional[conint(strict=True, le=65535, ge=0)] = Field(None, alias="DataSetWriterId")
    data_set_meta_data: Optional[DataSetMetaDataType] = Field(None, alias="DataSetMetaData")
    data_set_field_content_mask: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="DataSetFieldContentMask")
    message_receive_timeout: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="MessageReceiveTimeout")
    key_frame_count: Optional[conint(strict=True, le=4294967295, ge=0)] = Field(None, alias="KeyFrameCount")
    header_layout_uri: Optional[StrictStr] = Field(None, alias="HeaderLayoutUri")
    security_mode: Optional[StrictInt] = Field(None, alias="SecurityMode")
    security_group_id: Optional[StrictStr] = Field(None, alias="SecurityGroupId")
    security_key_services: Optional[conlist(EndpointDescription)] = Field(None, alias="SecurityKeyServices")
    data_set_reader_properties: Optional[conlist(KeyValuePair)] = Field(None, alias="DataSetReaderProperties")
    transport_settings: Optional[ExtensionObject] = Field(None, alias="TransportSettings")
    message_settings: Optional[ExtensionObject] = Field(None, alias="MessageSettings")
    subscribed_data_set: Optional[ExtensionObject] = Field(None, alias="SubscribedDataSet")
    __properties = ["Name", "Enabled", "PublisherId", "WriterGroupId", "DataSetWriterId", "DataSetMetaData", "DataSetFieldContentMask", "MessageReceiveTimeout", "KeyFrameCount", "HeaderLayoutUri", "SecurityMode", "SecurityGroupId", "SecurityKeyServices", "DataSetReaderProperties", "TransportSettings", "MessageSettings", "SubscribedDataSet"]

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
    def from_json(cls, json_str: str) -> DataSetReaderDataType:
        """Create an instance of DataSetReaderDataType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of publisher_id
        if self.publisher_id:
            _dict['PublisherId'] = self.publisher_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_set_meta_data
        if self.data_set_meta_data:
            _dict['DataSetMetaData'] = self.data_set_meta_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in security_key_services (list)
        _items = []
        if self.security_key_services:
            for _item in self.security_key_services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SecurityKeyServices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_set_reader_properties (list)
        _items = []
        if self.data_set_reader_properties:
            for _item in self.data_set_reader_properties:
                if _item:
                    _items.append(_item.to_dict())
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
    def from_dict(cls, obj: dict) -> DataSetReaderDataType:
        """Create an instance of DataSetReaderDataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataSetReaderDataType.parse_obj(obj)

        _obj = DataSetReaderDataType.parse_obj({
            "name": obj.get("Name"),
            "enabled": obj.get("Enabled"),
            "publisher_id": Variant.from_dict(obj.get("PublisherId")) if obj.get("PublisherId") is not None else None,
            "writer_group_id": obj.get("WriterGroupId"),
            "data_set_writer_id": obj.get("DataSetWriterId"),
            "data_set_meta_data": DataSetMetaDataType.from_dict(obj.get("DataSetMetaData")) if obj.get("DataSetMetaData") is not None else None,
            "data_set_field_content_mask": obj.get("DataSetFieldContentMask"),
            "message_receive_timeout": obj.get("MessageReceiveTimeout"),
            "key_frame_count": obj.get("KeyFrameCount"),
            "header_layout_uri": obj.get("HeaderLayoutUri"),
            "security_mode": obj.get("SecurityMode"),
            "security_group_id": obj.get("SecurityGroupId"),
            "security_key_services": [EndpointDescription.from_dict(_item) for _item in obj.get("SecurityKeyServices")] if obj.get("SecurityKeyServices") is not None else None,
            "data_set_reader_properties": [KeyValuePair.from_dict(_item) for _item in obj.get("DataSetReaderProperties")] if obj.get("DataSetReaderProperties") is not None else None,
            "transport_settings": ExtensionObject.from_dict(obj.get("TransportSettings")) if obj.get("TransportSettings") is not None else None,
            "message_settings": ExtensionObject.from_dict(obj.get("MessageSettings")) if obj.get("MessageSettings") is not None else None,
            "subscribed_data_set": ExtensionObject.from_dict(obj.get("SubscribedDataSet")) if obj.get("SubscribedDataSet") is not None else None
        })
        return _obj


