# coding: utf-8

"""
    OPC UA Web API

    Provides simple HTTPS based access to an OPC UA server.

    The version of the OpenAPI document: 1.05.4
    Contact: office@opcfoundation.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opcua_webapi.models.data_set_writer_data_type import DataSetWriterDataType

class TestDataSetWriterDataType(unittest.TestCase):
    """DataSetWriterDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSetWriterDataType:
        """Test DataSetWriterDataType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSetWriterDataType`
        """
        model = DataSetWriterDataType()
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
                            ua_type = 0, 
                            dimensions = [
                                0
                                ], ), )
                    ],
                transport_settings = opcua_webapi.models.transport_settings.TransportSettings(),
                message_settings = opcua_webapi.models.message_settings.MessageSettings()
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
