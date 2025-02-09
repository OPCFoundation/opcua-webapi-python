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

from opcua_webapi.models.eu_information import EUInformation

class TestEUInformation(unittest.TestCase):
    """EUInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EUInformation:
        """Test EUInformation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EUInformation`
        """
        model = EUInformation()
        if include_optional:
            return EUInformation(
                namespace_uri = '',
                unit_id = 56,
                display_name = opcua_webapi.models.localized_text.LocalizedText(
                    locale = '', 
                    text = '', ),
                description = opcua_webapi.models.localized_text.LocalizedText(
                    locale = '', 
                    text = '', )
            )
        else:
            return EUInformation(
        )
        """

    def testEUInformation(self):
        """Test EUInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
