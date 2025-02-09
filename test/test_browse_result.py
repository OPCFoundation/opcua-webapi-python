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

from opcua_webapi.models.browse_result import BrowseResult

class TestBrowseResult(unittest.TestCase):
    """BrowseResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrowseResult:
        """Test BrowseResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrowseResult`
        """
        model = BrowseResult()
        if include_optional:
            return BrowseResult(
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
                    ]
            )
        else:
            return BrowseResult(
        )
        """

    def testBrowseResult(self):
        """Test BrowseResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
