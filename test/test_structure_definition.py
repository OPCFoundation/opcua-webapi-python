# coding: utf-8

"""
    OPC UA Web API

    This API provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from opcua_webapi.models.structure_definition import StructureDefinition  # noqa: E501

class TestStructureDefinition(unittest.TestCase):
    """StructureDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StructureDefinition:
        """Test StructureDefinition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StructureDefinition`
        """
        model = StructureDefinition()  # noqa: E501
        if include_optional:
            return StructureDefinition(
                default_encoding_id = '',
                base_data_type = '',
                structure_type = 56,
                fields = [
                    opcua_webapi.models.structure_field.StructureField(
                        name = '', 
                        description = opcua_webapi.models.localized_text.LocalizedText(
                            locale = '', 
                            text = '', ), 
                        data_type = '', 
                        value_rank = 56, 
                        array_dimensions = [
                            0
                            ], 
                        max_string_length = 0, 
                        is_optional = True, )
                    ]
            )
        else:
            return StructureDefinition(
        )
        """

    def testStructureDefinition(self):
        """Test StructureDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
