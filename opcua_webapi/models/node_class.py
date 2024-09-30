# coding: utf-8

"""
    OPC UA Web API

    This API provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class NodeClass(int, Enum):
    """
    NodeClass
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_4 = 4
    NUMBER_8 = 8
    NUMBER_16 = 16
    NUMBER_32 = 32
    NUMBER_64 = 64
    NUMBER_128 = 128

    @classmethod
    def from_json(cls, json_str: str) -> NodeClass:
        """Create an instance of NodeClass from a JSON string"""
        return NodeClass(json.loads(json_str))


