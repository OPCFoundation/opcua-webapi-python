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

from opcua_webapi.models.update_structure_data_details import UpdateStructureDataDetails

class TestUpdateStructureDataDetails(unittest.TestCase):
    """UpdateStructureDataDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateStructureDataDetails:
        """Test UpdateStructureDataDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateStructureDataDetails`
        """
        model = UpdateStructureDataDetails()
        if include_optional:
            return UpdateStructureDataDetails(
                node_id = '',
                perform_insert_replace = 56,
                update_values = [
                    opcua_webapi.models.data_value.DataValue(
                        ua_type = 0, 
                        value = null, 
                        dimensions = [
                            0
                            ], 
                        status_code = opcua_webapi.models.status_code.StatusCode(
                            code = 0, 
                            symbol = '', ), 
                        source_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        source_picoseconds = 0, 
                        server_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        server_picoseconds = 0, )
                    ]
            )
        else:
            return UpdateStructureDataDetails(
        )
        """

    def testUpdateStructureDataDetails(self):
        """Test UpdateStructureDataDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
