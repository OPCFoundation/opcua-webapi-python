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

from opcua_webapi.models.monitored_item_create_result import MonitoredItemCreateResult  # noqa: E501

class TestMonitoredItemCreateResult(unittest.TestCase):
    """MonitoredItemCreateResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MonitoredItemCreateResult:
        """Test MonitoredItemCreateResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MonitoredItemCreateResult`
        """
        model = MonitoredItemCreateResult()  # noqa: E501
        if include_optional:
            return MonitoredItemCreateResult(
                status_code = 0,
                monitored_item_id = 0,
                revised_sampling_interval = 1.337,
                revised_queue_size = 0,
                filter_result = opcua_webapi.models.extension_object.ExtensionObject(
                    type_id = '', 
                    encoding = 0, 
                    body = opcua_webapi.models.body.Body(), )
            )
        else:
            return MonitoredItemCreateResult(
        )
        """

    def testMonitoredItemCreateResult(self):
        """Test MonitoredItemCreateResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
