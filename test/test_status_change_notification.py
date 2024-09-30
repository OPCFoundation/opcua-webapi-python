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

from opcua_webapi.models.status_change_notification import StatusChangeNotification  # noqa: E501

class TestStatusChangeNotification(unittest.TestCase):
    """StatusChangeNotification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatusChangeNotification:
        """Test StatusChangeNotification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatusChangeNotification`
        """
        model = StatusChangeNotification()  # noqa: E501
        if include_optional:
            return StatusChangeNotification(
                status = 0,
                diagnostic_info = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
                    symbolic_id = 56, 
                    namespace_uri = 56, 
                    locale = 56, 
                    localized_text = 56, 
                    additional_info = '', 
                    inner_status_code = 0, 
                    inner_diagnostic_info = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
                        symbolic_id = 56, 
                        namespace_uri = 56, 
                        locale = 56, 
                        localized_text = 56, 
                        additional_info = '', 
                        inner_status_code = 0, ), )
            )
        else:
            return StatusChangeNotification(
        )
        """

    def testStatusChangeNotification(self):
        """Test StatusChangeNotification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
