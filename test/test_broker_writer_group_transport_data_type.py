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

from opcua_webapi.models.broker_writer_group_transport_data_type import BrokerWriterGroupTransportDataType

class TestBrokerWriterGroupTransportDataType(unittest.TestCase):
    """BrokerWriterGroupTransportDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrokerWriterGroupTransportDataType:
        """Test BrokerWriterGroupTransportDataType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrokerWriterGroupTransportDataType`
        """
        model = BrokerWriterGroupTransportDataType()
        if include_optional:
            return BrokerWriterGroupTransportDataType(
                queue_name = '',
                resource_uri = '',
                authentication_profile_uri = '',
                requested_delivery_guarantee = 56
            )
        else:
            return BrokerWriterGroupTransportDataType(
        )
        """

    def testBrokerWriterGroupTransportDataType(self):
        """Test BrokerWriterGroupTransportDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
