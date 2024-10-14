# BrokerWriterGroupTransportDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_name** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 
**authentication_profile_uri** | **str** |  | [optional] 
**requested_delivery_guarantee** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.broker_writer_group_transport_data_type import BrokerWriterGroupTransportDataType

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerWriterGroupTransportDataType from a JSON string
broker_writer_group_transport_data_type_instance = BrokerWriterGroupTransportDataType.from_json(json)
# print the JSON string representation of the object
print(BrokerWriterGroupTransportDataType.to_json())

# convert the object into a dict
broker_writer_group_transport_data_type_dict = broker_writer_group_transport_data_type_instance.to_dict()
# create an instance of BrokerWriterGroupTransportDataType from a dict
broker_writer_group_transport_data_type_from_dict = BrokerWriterGroupTransportDataType.from_dict(broker_writer_group_transport_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


