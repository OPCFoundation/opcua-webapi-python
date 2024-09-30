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

from opcua_webapi.models.json_data_set_writer_message_data_type import JsonDataSetWriterMessageDataType  # noqa: E501

class TestJsonDataSetWriterMessageDataType(unittest.TestCase):
    """JsonDataSetWriterMessageDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonDataSetWriterMessageDataType:
        """Test JsonDataSetWriterMessageDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonDataSetWriterMessageDataType`
        """
        model = JsonDataSetWriterMessageDataType()  # noqa: E501
        if include_optional:
            return JsonDataSetWriterMessageDataType(
                data_set_message_content_mask = 0
            )
        else:
            return JsonDataSetWriterMessageDataType(
        )
        """

    def testJsonDataSetWriterMessageDataType(self):
        """Test JsonDataSetWriterMessageDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
