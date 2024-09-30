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

from opcua_webapi.models.create_session_request import CreateSessionRequest  # noqa: E501

class TestCreateSessionRequest(unittest.TestCase):
    """CreateSessionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSessionRequest:
        """Test CreateSessionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSessionRequest`
        """
        model = CreateSessionRequest()  # noqa: E501
        if include_optional:
            return CreateSessionRequest(
                request_header = opcua_webapi.models.request_header.RequestHeader(
                    authentication_token = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    request_handle = 0, 
                    return_diagnostics = 0, 
                    audit_entry_id = '', 
                    timeout_hint = 0, 
                    additional_header = opcua_webapi.models.extension_object.ExtensionObject(
                        type_id = '', 
                        encoding = 0, 
                        body = opcua_webapi.models.body.Body(), ), ),
                client_description = opcua_webapi.models.application_description.ApplicationDescription(
                    application_uri = '', 
                    product_uri = '', 
                    application_name = opcua_webapi.models.localized_text.LocalizedText(
                        locale = '', 
                        text = '', ), 
                    application_type = 56, 
                    gateway_server_uri = '', 
                    discovery_profile_uri = '', 
                    discovery_urls = [
                        ''
                        ], ),
                server_uri = '',
                endpoint_url = '',
                session_name = '',
                client_nonce = 'YQ==',
                client_certificate = 'YQ==',
                requested_session_timeout = 1.337,
                max_response_message_size = 0
            )
        else:
            return CreateSessionRequest(
        )
        """

    def testCreateSessionRequest(self):
        """Test CreateSessionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
