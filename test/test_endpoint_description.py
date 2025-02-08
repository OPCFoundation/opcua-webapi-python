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

from opcua_webapi.models.endpoint_description import EndpointDescription

class TestEndpointDescription(unittest.TestCase):
    """EndpointDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointDescription:
        """Test EndpointDescription
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointDescription`
        """
        model = EndpointDescription()
        if include_optional:
            return EndpointDescription(
                endpoint_url = '',
                server = opcua_webapi.models.application_description.ApplicationDescription(
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
                server_certificate = 'YQ==',
                security_mode = 56,
                security_policy_uri = '',
                user_identity_tokens = [
                    opcua_webapi.models.user_token_policy.UserTokenPolicy(
                        policy_id = '', 
                        token_type = 56, 
                        issued_token_type = '', 
                        issuer_endpoint_url = '', 
                        security_policy_uri = '', )
                    ],
                transport_profile_uri = '',
                security_level = 0
            )
        else:
            return EndpointDescription(
        )
        """

    def testEndpointDescription(self):
        """Test EndpointDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
