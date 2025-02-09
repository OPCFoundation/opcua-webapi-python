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

from opcua_webapi.models.json_network_message import JsonNetworkMessage

class TestJsonNetworkMessage(unittest.TestCase):
    """JsonNetworkMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonNetworkMessage:
        """Test JsonNetworkMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonNetworkMessage`
        """
        model = JsonNetworkMessage()
        if include_optional:
            return JsonNetworkMessage(
                message_id = '',
                message_type = '',
                publisher_id = '',
                writer_group_name = '',
                data_set_class_id = '',
                messages = None
            )
        else:
            return JsonNetworkMessage(
        )
        """

    def testJsonNetworkMessage(self):
        """Test JsonNetworkMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
