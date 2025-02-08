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

from opcua_webapi.models.browse_response import BrowseResponse

class TestBrowseResponse(unittest.TestCase):
    """BrowseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrowseResponse:
        """Test BrowseResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrowseResponse`
        """
        model = BrowseResponse()
        if include_optional:
            return BrowseResponse(
                response_header = opcua_webapi.models.response_header.ResponseHeader(
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    request_handle = 0, 
                    service_result = opcua_webapi.models.status_code.StatusCode(
                        code = 0, 
                        symbol = '', ), 
                    service_diagnostics = opcua_webapi.models.diagnostic_info.DiagnosticInfo(
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
                            additional_info = '', ), ), 
                    string_table = [
                        ''
                        ], 
                    additional_header = opcua_webapi.models.extension_object.ExtensionObject(
                        ua_type_id = '', 
                        ua_encoding = 0, 
                        ua_body = 'YQ==', ), ),
                results = [
                    opcua_webapi.models.browse_result.BrowseResult(
                        status_code = opcua_webapi.models.status_code.StatusCode(
                            code = 0, 
                            symbol = '', ), 
                        continuation_point = 'YQ==', 
                        references = [
                            opcua_webapi.models.reference_description.ReferenceDescription(
                                reference_type_id = '', 
                                is_forward = True, 
                                node_id = '', 
                                browse_name = '', 
                                display_name = opcua_webapi.models.localized_text.LocalizedText(
                                    locale = '', 
                                    text = '', ), 
                                node_class = 56, 
                                type_definition = '', )
                            ], )
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
            return BrowseResponse(
        )
        """

    def testBrowseResponse(self):
        """Test BrowseResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
