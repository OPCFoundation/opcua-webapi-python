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

from opcua_webapi.models.history_update_result import HistoryUpdateResult

class TestHistoryUpdateResult(unittest.TestCase):
    """HistoryUpdateResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HistoryUpdateResult:
        """Test HistoryUpdateResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HistoryUpdateResult`
        """
        model = HistoryUpdateResult()
        if include_optional:
            return HistoryUpdateResult(
                status_code = opcua_webapi.models.status_code.StatusCode(
                    code = 0, 
                    symbol = '', ),
                operation_results = [
                    opcua_webapi.models.status_code.StatusCode(
                        code = 0, 
                        symbol = '', )
                    ],
                diagnostic_infos = [
                    opcua_webapi.models.diagnostic_info.DiagnosticInfo(
                        symbolic_id = 56, 
                        namespace_uri = 56, 
                        locale = 56, 
                        localized_text = 56, 
                        additional_info = '', 
                        inner_status_code = opcua_webapi.models.status_code.StatusCode(
                            code = 0, 
                            symbol = '', ), 
                        inner_diagnostic_info = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
                            symbolic_id = 56, 
                            namespace_uri = 56, 
                            locale = 56, 
                            localized_text = 56, 
                            additional_info = '', ), )
                    ]
            )
        else:
            return HistoryUpdateResult(
        )
        """

    def testHistoryUpdateResult(self):
        """Test HistoryUpdateResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
