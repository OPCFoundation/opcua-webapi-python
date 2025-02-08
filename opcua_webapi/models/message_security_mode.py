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


class MessageSecurityMode(int, Enum):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.3.10).
    """

    """
    allowed enum values
    """
    Invalid = 0
    NoSignOrEncrypt = 1
    Sign = 2
    SignAndEncrypt = 3

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageSecurityMode from a JSON string"""
        return cls(json.loads(json_str))


