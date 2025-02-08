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

from opcua_webapi.models.issued_identity_token import IssuedIdentityToken

class TestIssuedIdentityToken(unittest.TestCase):
    """IssuedIdentityToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IssuedIdentityToken:
        """Test IssuedIdentityToken
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IssuedIdentityToken`
        """
        model = IssuedIdentityToken()
        if include_optional:
            return IssuedIdentityToken(
                token_data = 'YQ==',
                encryption_algorithm = '',
                policy_id = ''
            )
        else:
            return IssuedIdentityToken(
        )
        """

    def testIssuedIdentityToken(self):
        """Test IssuedIdentityToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
