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

from opcua_webapi.models.signature_data import SignatureData

class TestSignatureData(unittest.TestCase):
    """SignatureData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignatureData:
        """Test SignatureData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignatureData`
        """
        model = SignatureData()
        if include_optional:
            return SignatureData(
                algorithm = '',
                signature = 'YQ=='
            )
        else:
            return SignatureData(
        )
        """

    def testSignatureData(self):
        """Test SignatureData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
