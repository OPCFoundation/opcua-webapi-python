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

from opcua_webapi.models.history_update_request import HistoryUpdateRequest

class TestHistoryUpdateRequest(unittest.TestCase):
    """HistoryUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HistoryUpdateRequest:
        """Test HistoryUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HistoryUpdateRequest`
        """
        model = HistoryUpdateRequest()
        if include_optional:
            return HistoryUpdateRequest(
                request_header = opcua_webapi.models.request_header.RequestHeader(
                    authentication_token = '', 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    request_handle = 0, 
                    return_diagnostics = 0, 
                    audit_entry_id = '', 
                    timeout_hint = 0, 
                    additional_header = opcua_webapi.models.extension_object.ExtensionObject(
                        ua_type_id = '', 
                        ua_encoding = 0, 
                        ua_body = 'YQ==', ), ),
                history_update_details = [
                    opcua_webapi.models.extension_object.ExtensionObject(
                        ua_type_id = '', 
                        ua_encoding = 0, 
                        ua_body = 'YQ==', )
                    ]
            )
        else:
            return HistoryUpdateRequest(
        )
        """

    def testHistoryUpdateRequest(self):
        """Test HistoryUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
