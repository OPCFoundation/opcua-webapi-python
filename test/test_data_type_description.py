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

from opcua_webapi.models.data_type_description import DataTypeDescription  # noqa: E501

class TestDataTypeDescription(unittest.TestCase):
    """DataTypeDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataTypeDescription:
        """Test DataTypeDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataTypeDescription`
        """
        model = DataTypeDescription()  # noqa: E501
        if include_optional:
            return DataTypeDescription(
                data_type_id = '',
                name = ''
            )
        else:
            return DataTypeDescription(
        )
        """

    def testDataTypeDescription(self):
        """Test DataTypeDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
