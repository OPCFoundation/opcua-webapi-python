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

from opcua_webapi.models.event_notification_list import EventNotificationList  # noqa: E501

class TestEventNotificationList(unittest.TestCase):
    """EventNotificationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventNotificationList:
        """Test EventNotificationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventNotificationList`
        """
        model = EventNotificationList()  # noqa: E501
        if include_optional:
            return EventNotificationList(
                events = [
                    opcua_webapi.models.event_field_list.EventFieldList(
                        client_handle = 0, 
                        event_fields = [
                            opcua_webapi.models.variant.Variant(
                                type = 0, 
                                body = null, 
                                dimensions = [
                                    0
                                    ], )
                            ], )
                    ]
            )
        else:
            return EventNotificationList(
        )
        """

    def testEventNotificationList(self):
        """Test EventNotificationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()