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

from opcua_webapi.models.data_set_writer_data_type import DataSetWriterDataType  # noqa: E501

class TestDataSetWriterDataType(unittest.TestCase):
    """DataSetWriterDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSetWriterDataType:
        """Test DataSetWriterDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSetWriterDataType`
        """
        model = DataSetWriterDataType()  # noqa: E501
        if include_optional:
            return DataSetWriterDataType(
                name = '',
                enabled = True,
                data_set_writer_id = 0,
                data_set_field_content_mask = 0,
                key_frame_count = 0,
                data_set_name = '',
                data_set_writer_properties = [
                    opcua_webapi.models.key_value_pair.KeyValuePair(
                        key = '', 
                        value = opcua_webapi.models.variant.Variant(
                            type = 0, 
                            body = null, 
                            dimensions = [
                                0
                                ], ), )
                    ],
                transport_settings = opcua_webapi.models.extension_object.ExtensionObject(
                    type_id = '', 
                    encoding = 0, 
                    body = opcua_webapi.models.body.Body(), ),
                message_settings = opcua_webapi.models.extension_object.ExtensionObject(
                    type_id = '', 
                    encoding = 0, 
                    body = opcua_webapi.models.body.Body(), )
            )
        else:
            return DataSetWriterDataType(
        )
        """

    def testDataSetWriterDataType(self):
        """Test DataSetWriterDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()