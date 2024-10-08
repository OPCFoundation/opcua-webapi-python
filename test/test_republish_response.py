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

from opcua_webapi.models.republish_response import RepublishResponse  # noqa: E501

class TestRepublishResponse(unittest.TestCase):
    """RepublishResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepublishResponse:
        """Test RepublishResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepublishResponse`
        """
        model = RepublishResponse()  # noqa: E501
        if include_optional:
            return RepublishResponse(
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
                notification_message = opcua_webapi.models.notification_message.NotificationMessage(
                    sequence_number = 0, 
                    publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    notification_data = [
                        opcua_webapi.models.extension_object.ExtensionObject(
                            type_id = '', 
                            encoding = 0, 
                            body = opcua_webapi.models.body.Body(), )
                        ], )
            )
        else:
            return RepublishResponse(
        )
        """

    def testRepublishResponse(self):
        """Test RepublishResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
