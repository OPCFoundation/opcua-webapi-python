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

from opcua_webapi.models.security_group_data_type import SecurityGroupDataType  # noqa: E501

class TestSecurityGroupDataType(unittest.TestCase):
    """SecurityGroupDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityGroupDataType:
        """Test SecurityGroupDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityGroupDataType`
        """
        model = SecurityGroupDataType()  # noqa: E501
        if include_optional:
            return SecurityGroupDataType(
                name = '',
                security_group_folder = [
                    ''
                    ],
                key_lifetime = 1.337,
                security_policy_uri = '',
                max_future_key_count = 0,
                max_past_key_count = 0,
                security_group_id = '',
                role_permissions = [
                    opcua_webapi.models.role_permission_type.RolePermissionType(
                        role_id = '', 
                        permissions = 0, )
                    ],
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
            return SecurityGroupDataType(
        )
        """

    def testSecurityGroupDataType(self):
        """Test SecurityGroupDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()