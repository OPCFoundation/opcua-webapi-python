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

from opcua_webapi.models.read_annotation_data_details import ReadAnnotationDataDetails  # noqa: E501

class TestReadAnnotationDataDetails(unittest.TestCase):
    """ReadAnnotationDataDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadAnnotationDataDetails:
        """Test ReadAnnotationDataDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadAnnotationDataDetails`
        """
        model = ReadAnnotationDataDetails()  # noqa: E501
        if include_optional:
            return ReadAnnotationDataDetails(
                req_times = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ]
            )
        else:
            return ReadAnnotationDataDetails(
        )
        """

    def testReadAnnotationDataDetails(self):
        """Test ReadAnnotationDataDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
