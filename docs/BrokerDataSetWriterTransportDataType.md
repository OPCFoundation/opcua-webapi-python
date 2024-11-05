# BrokerDataSetWriterTransportDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_name** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 
**authentication_profile_uri** | **str** |  | [optional] 
**requested_delivery_guarantee** | **int** |  | [optional] 
**meta_data_queue_name** | **str** |  | [optional] 
**meta_data_update_time** | **float** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.broker_data_set_writer_transport_data_type import BrokerDataSetWriterTransportDataType

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerDataSetWriterTransportDataType from a JSON string
broker_data_set_writer_transport_data_type_instance = BrokerDataSetWriterTransportDataType.from_json(json)
# print the JSON string representation of the object
print(BrokerDataSetWriterTransportDataType.to_json())

# convert the object into a dict
broker_data_set_writer_transport_data_type_dict = broker_data_set_writer_transport_data_type_instance.to_dict()
# create an instance of BrokerDataSetWriterTransportDataType from a dict
broker_data_set_writer_transport_data_type_from_dict = BrokerDataSetWriterTransportDataType.from_dict(broker_data_set_writer_transport_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


