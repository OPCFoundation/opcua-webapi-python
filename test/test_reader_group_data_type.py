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

from opcua_webapi.models.reader_group_data_type import ReaderGroupDataType

class TestReaderGroupDataType(unittest.TestCase):
    """ReaderGroupDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReaderGroupDataType:
        """Test ReaderGroupDataType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReaderGroupDataType`
        """
        model = ReaderGroupDataType()
        if include_optional:
            return ReaderGroupDataType(
                transport_settings = opcua_webapi.models.transport_settings.TransportSettings(),
                message_settings = opcua_webapi.models.message_settings.MessageSettings(),
                data_set_readers = [
                    opcua_webapi.models.data_set_reader_data_type.DataSetReaderDataType(
                        name = '', 
                        enabled = True, 
                        publisher_id = opcua_webapi.models.variant.Variant(
                            ua_type = 0, 
                            value = null, 
                            dimensions = [
                                0
                                ], ), 
                        writer_group_id = 0, 
                        data_set_writer_id = 0, 
                        data_set_meta_data = opcua_webapi.models.data_set_meta_data_type.DataSetMetaDataType(
                            name = '', 
                            description = opcua_webapi.models.localized_text.LocalizedText(
                                locale = '', 
                                text = '', ), 
                            fields = [
                                opcua_webapi.models.field_meta_data.FieldMetaData(
                                    name = '', 
                                    field_flags = 0, 
                                    built_in_type = 0, 
                                    data_type = '', 
                                    value_rank = 56, 
                                    array_dimensions = [
                                        0
                                        ], 
                                    max_string_length = 0, 
                                    data_set_field_id = '', 
                                    properties = [
                                        opcua_webapi.models.key_value_pair.KeyValuePair(
                                            key = '', 
                                            value = opcua_webapi.models.variant.Variant(
                                                ua_type = 0, ), )
                                        ], )
                                ], 
                            data_set_class_id = '', 
                            configuration_version = opcua_webapi.models.configuration_version_data_type.ConfigurationVersionDataType(
                                major_version = 0, 
                                minor_version = 0, ), ), 
                        data_set_field_content_mask = 0, 
                        message_receive_timeout = 1.337, 
                        key_frame_count = 0, 
                        header_layout_uri = '', 
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
                        data_set_reader_properties = [
                            opcua_webapi.models.key_value_pair.KeyValuePair(
                                key = '', )
                            ], 
                        transport_settings = opcua_webapi.models.transport_settings.TransportSettings(), 
                        message_settings = opcua_webapi.models.message_settings.MessageSettings(), 
                        subscribed_data_set = opcua_webapi.models.subscribed_data_set.SubscribedDataSet(), )
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
                            ua_type = 0, 
                            dimensions = [
                                0
                                ], ), )
                    ]
            )
        else:
            return ReaderGroupDataType(
        )
        """

    def testReaderGroupDataType(self):
        """Test ReaderGroupDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
