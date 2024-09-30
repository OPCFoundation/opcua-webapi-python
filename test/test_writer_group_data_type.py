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

from opcua_webapi.models.writer_group_data_type import WriterGroupDataType  # noqa: E501

class TestWriterGroupDataType(unittest.TestCase):
    """WriterGroupDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WriterGroupDataType:
        """Test WriterGroupDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WriterGroupDataType`
        """
        model = WriterGroupDataType()  # noqa: E501
        if include_optional:
            return WriterGroupDataType(
                writer_group_id = 0,
                publishing_interval = 1.337,
                keep_alive_time = 1.337,
                priority = 0,
                locale_ids = [
                    ''
                    ],
                header_layout_uri = '',
                transport_settings = opcua_webapi.models.extension_object.ExtensionObject(
                    type_id = '', 
                    encoding = 0, 
                    body = opcua_webapi.models.body.Body(), ),
                message_settings = opcua_webapi.models.extension_object.ExtensionObject(
                    type_id = '', 
                    encoding = 0, 
                    body = opcua_webapi.models.body.Body(), ),
                data_set_writers = [
                    opcua_webapi.models.data_set_writer_data_type.DataSetWriterDataType(
                        name = '', 
                        enabled = True, 
                        data_set_writer_id = 0, 
                        data_set_field_content_mask = 0, 
                        key_frame_count = 0, 
                        data_set_name = '', 
                        data_set_writer_properties = [
                            opcua_webapi.models.key_value_pair.KeyValuePair(
                                key = '', 
                                value = opcua_webapi.models.variant.Variant(
                                    type = 0, 
                                    body = null, 
                                    dimensions = [
                                        0
                                        ], ), )
                            ], 
                        transport_settings = opcua_webapi.models.extension_object.ExtensionObject(
                            type_id = '', 
                            encoding = 0, 
                            body = opcua_webapi.models.body.Body(), ), 
                        message_settings = opcua_webapi.models.extension_object.ExtensionObject(
                            type_id = '', 
                            encoding = 0, 
                            body = opcua_webapi.models.body.Body(), ), )
                    ],
                name = '',
                enabled = True,
                security_mode = 56,
                security_group_id = '',
                security_key_services = [
                    opcua_webapi.models.endpoint_description.EndpointDescription(
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
                        security_level = 0, )
                    ],
                max_network_message_size = 0,
                group_properties = [
                    opcua_webapi.models.key_value_pair.KeyValuePair(
                        key = '', 
                        value = opcua_webapi.models.variant.Variant(
                            type = 0, 
                            body = null, 
                            dimensions = [
                                0
                                ], ), )
                    ]
            )
        else:
            return WriterGroupDataType(
        )
        """

    def testWriterGroupDataType(self):
        """Test WriterGroupDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
