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
import json
from enum import Enum
from typing_extensions import Self


class JsonDataSetMessageContentMaskBits(int, Enum):
    """
    JsonDataSetMessageContentMaskBits
    """

    """
    allowed enum values
    """
    DataSetWriterId = 1
    MetaDataVersion = 2
    SequenceNumber = 4
    Timestamp = 8
    Status = 16
    MessageType = 32
    DataSetWriterName = 64
    FieldEncoding1 = 128
    PublisherId = 256
    WriterGroupName = 512
    MinorVersion = 1024
    FieldEncoding2 = 2048

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JsonDataSetMessageContentMaskBits from a JSON string"""
        return cls(json.loads(json_str))

