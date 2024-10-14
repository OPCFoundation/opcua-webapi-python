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

from opcua_webapi.models.monitored_item_create_request import MonitoredItemCreateRequest  # noqa: E501

class TestMonitoredItemCreateRequest(unittest.TestCase):
    """MonitoredItemCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MonitoredItemCreateRequest:
        """Test MonitoredItemCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MonitoredItemCreateRequest`
        """
        model = MonitoredItemCreateRequest()  # noqa: E501
        if include_optional:
            return MonitoredItemCreateRequest(
                item_to_monitor = opcua_webapi.models.read_value_id.ReadValueId(
                    node_id = '', 
                    attribute_id = 0, 
                    index_range = '', 
                    data_encoding = '', ),
                monitoring_mode = 56,
                requested_parameters = opcua_webapi.models.monitoring_parameters.MonitoringParameters(
                    client_handle = 0, 
                    sampling_interval = 1.337, 
                    filter = opcua_webapi.models.extension_object.ExtensionObject(
                        type_id = '', 
                        encoding = 0, 
                        body = opcua_webapi.models.body.Body(), ), 
                    queue_size = 0, 
                    discard_oldest = True, )
            )
        else:
            return MonitoredItemCreateRequest(
        )
        """

    def testMonitoredItemCreateRequest(self):
        """Test MonitoredItemCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()