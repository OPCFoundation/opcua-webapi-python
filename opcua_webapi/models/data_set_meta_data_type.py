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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opcua_webapi.models.configuration_version_data_type import ConfigurationVersionDataType
from opcua_webapi.models.enum_description import EnumDescription
from opcua_webapi.models.field_meta_data import FieldMetaData
from opcua_webapi.models.localized_text import LocalizedText
from opcua_webapi.models.simple_type_description import SimpleTypeDescription
from opcua_webapi.models.structure_description import StructureDescription
from typing import Optional, Set
from typing_extensions import Self

class DataSetMetaDataType(BaseModel):
    """
    [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.3/#6.2.3.2.3).
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    description: Optional[LocalizedText] = Field(default=None, alias="Description")
    fields: Optional[List[FieldMetaData]] = Field(default=None, alias="Fields")
    data_set_class_id: Optional[StrictStr] = Field(default=None, alias="DataSetClassId")
    configuration_version: Optional[ConfigurationVersionDataType] = Field(default=None, alias="ConfigurationVersion")
    namespaces: Optional[List[StrictStr]] = Field(default=None, alias="Namespaces")
    structure_data_types: Optional[List[StructureDescription]] = Field(default=None, alias="StructureDataTypes")
    enum_data_types: Optional[List[EnumDescription]] = Field(default=None, alias="EnumDataTypes")
    simple_data_types: Optional[List[SimpleTypeDescription]] = Field(default=None, alias="SimpleDataTypes")
    __properties: ClassVar[List[str]] = ["Namespaces", "StructureDataTypes", "EnumDataTypes", "SimpleDataTypes"]

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
        """Create an instance of DataSetMetaDataType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in structure_data_types (list)
        _items = []
        if self.structure_data_types:
            for _item_structure_data_types in self.structure_data_types:
                if _item_structure_data_types:
                    _items.append(_item_structure_data_types.to_dict())
            _dict['StructureDataTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in enum_data_types (list)
        _items = []
        if self.enum_data_types:
            for _item_enum_data_types in self.enum_data_types:
                if _item_enum_data_types:
                    _items.append(_item_enum_data_types.to_dict())
            _dict['EnumDataTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in simple_data_types (list)
        _items = []
        if self.simple_data_types:
            for _item_simple_data_types in self.simple_data_types:
                if _item_simple_data_types:
                    _items.append(_item_simple_data_types.to_dict())
            _dict['SimpleDataTypes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataSetMetaDataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Namespaces": obj.get("Namespaces"),
            "StructureDataTypes": [StructureDescription.from_dict(_item) for _item in obj["StructureDataTypes"]] if obj.get("StructureDataTypes") is not None else None,
            "EnumDataTypes": [EnumDescription.from_dict(_item) for _item in obj["EnumDataTypes"]] if obj.get("EnumDataTypes") is not None else None,
            "SimpleDataTypes": [SimpleTypeDescription.from_dict(_item) for _item in obj["SimpleDataTypes"]] if obj.get("SimpleDataTypes") is not None else None
        })
        return _obj


