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

from opcua_webapi.models.modify_subscription_response import ModifySubscriptionResponse  # noqa: E501

class TestModifySubscriptionResponse(unittest.TestCase):
    """ModifySubscriptionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModifySubscriptionResponse:
        """Test ModifySubscriptionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModifySubscriptionResponse`
        """
        model = ModifySubscriptionResponse()  # noqa: E501
        if include_optional:
            return ModifySubscriptionResponse(
                response_header = opcua_webapi.models.response_header.ResponseHeader(
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    request_handle = 0, 
                    service_result = 0, 
                    service_diagnostics = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
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
                            inner_status_code = 0, ), ), 
                    string_table = [
                        ''
                        ], 
                    additional_header = opcua_webapi.models.extension_object.ExtensionObject(
                        type_id = '', 
                        encoding = 0, 
                        body = opcua_webapi.models.body.Body(), ), ),
                revised_publishing_interval = 1.337,
                revised_lifetime_count = 0,
                revised_max_keep_alive_count = 0
            )
        else:
            return ModifySubscriptionResponse(
        )
        """

    def testModifySubscriptionResponse(self):
        """Test ModifySubscriptionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
