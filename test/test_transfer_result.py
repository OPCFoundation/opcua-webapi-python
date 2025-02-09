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

from opcua_webapi.models.transfer_result import TransferResult

class TestTransferResult(unittest.TestCase):
    """TransferResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferResult:
        """Test TransferResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferResult`
        """
        model = TransferResult()
        if include_optional:
            return TransferResult(
                status_code = opcua_webapi.models.status_code.StatusCode(
                    code = 0, 
                    symbol = '', ),
                available_sequence_numbers = [
                    0
                    ]
            )
        else:
            return TransferResult(
        )
        """

    def testTransferResult(self):
        """Test TransferResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
