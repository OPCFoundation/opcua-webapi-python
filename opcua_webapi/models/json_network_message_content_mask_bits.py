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


class JsonNetworkMessageContentMaskBits(int, Enum):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.3.2/#6.3.2.1.1).
    """

    """
    allowed enum values
    """
    NetworkMessageHeader = 1
    DataSetMessageHeader = 2
    SingleDataSetMessage = 4
    PublisherId = 8
    DataSetClassId = 16
    ReplyTo = 32
    WriterGroupName = 64

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JsonNetworkMessageContentMaskBits from a JSON string"""
        return cls(json.loads(json_str))


