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

from opcua_webapi.models.pub_sub_key_push_target_data_type import PubSubKeyPushTargetDataType  # noqa: E501

class TestPubSubKeyPushTargetDataType(unittest.TestCase):
    """PubSubKeyPushTargetDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PubSubKeyPushTargetDataType:
        """Test PubSubKeyPushTargetDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PubSubKeyPushTargetDataType`
        """
        model = PubSubKeyPushTargetDataType()  # noqa: E501
        if include_optional:
            return PubSubKeyPushTargetDataType(
                application_uri = '',
                push_target_folder = [
                    ''
                    ],
                endpoint_url = '',
                security_policy_uri = '',
                user_token_type = opcua_webapi.models.user_token_policy.UserTokenPolicy(
                    policy_id = '', 
                    token_type = 56, 
                    issued_token_type = '', 
                    issuer_endpoint_url = '', 
                    security_policy_uri = '', ),
                requested_key_count = 0,
                retry_interval = 1.337,
                push_target_properties = [
                    opcua_webapi.models.key_value_pair.KeyValuePair(
                        key = '', 
                        value = opcua_webapi.models.variant.Variant(
                            type = 0, 
                            body = null, 
                            dimensions = [
                                0
                                ], ), )
                    ],
                security_groups = [
                    ''
                    ]
            )
        else:
            return PubSubKeyPushTargetDataType(
        )
        """

    def testPubSubKeyPushTargetDataType(self):
        """Test PubSubKeyPushTargetDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
