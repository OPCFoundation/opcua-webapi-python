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

from opcua_webapi.models.attribute_operand import AttributeOperand

class TestAttributeOperand(unittest.TestCase):
    """AttributeOperand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeOperand:
        """Test AttributeOperand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeOperand`
        """
        model = AttributeOperand()
        if include_optional:
            return AttributeOperand(
                node_id = '',
                alias = '',
                browse_path = opcua_webapi.models.relative_path.RelativePath(
                    elements = [
                        opcua_webapi.models.relative_path_element.RelativePathElement(
                            reference_type_id = '', 
                            is_inverse = True, 
                            include_subtypes = True, 
                            target_name = '', )
                        ], ),
                attribute_id = 0,
                index_range = ''
            )
        else:
            return AttributeOperand(
        )
        """

    def testAttributeOperand(self):
        """Test AttributeOperand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
