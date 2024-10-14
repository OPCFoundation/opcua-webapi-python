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

from opcua_webapi.models.read_event_details import ReadEventDetails  # noqa: E501

class TestReadEventDetails(unittest.TestCase):
    """ReadEventDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadEventDetails:
        """Test ReadEventDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadEventDetails`
        """
        model = ReadEventDetails()  # noqa: E501
        if include_optional:
            return ReadEventDetails(
                num_values_per_node = 0,
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                filter = opcua_webapi.models.event_filter.EventFilter(
                    select_clauses = [
                        opcua_webapi.models.simple_attribute_operand.SimpleAttributeOperand(
                            type_definition_id = '', 
                            browse_path = [
                                ''
                                ], 
                            attribute_id = 0, 
                            index_range = '', )
                        ], 
                    where_clause = opcua_webapi.models.content_filter.ContentFilter(
                        elements = [
                            opcua_webapi.models.content_filter_element.ContentFilterElement(
                                filter_operator = 56, 
                                filter_operands = [
                                    opcua_webapi.models.extension_object.ExtensionObject(
                                        type_id = '', 
                                        encoding = 0, 
                                        body = opcua_webapi.models.body.Body(), )
                                    ], )
                            ], ), )
            )
        else:
            return ReadEventDetails(
        )
        """

    def testReadEventDetails(self):
        """Test ReadEventDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()