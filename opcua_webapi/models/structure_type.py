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


class StructureType(int, Enum):
    """
    StructureType
    """

    """
    allowed enum values
    """
    Structure = 0
    StructureWithOptionalFields = 1
    Union = 2
    StructureWithSubtypedValues = 3
    UnionWithSubtypedValues = 4

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StructureType from a JSON string"""
        return cls(json.loads(json_str))


