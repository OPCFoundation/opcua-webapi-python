# BrokerConnectionTransportDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uri** | **str** |  | [optional] 
**authentication_profile_uri** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.broker_connection_transport_data_type import BrokerConnectionTransportDataType

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerConnectionTransportDataType from a JSON string
broker_connection_transport_data_type_instance = BrokerConnectionTransportDataType.from_json(json)
# print the JSON string representation of the object
print(BrokerConnectionTransportDataType.to_json())

# convert the object into a dict
broker_connection_transport_data_type_dict = broker_connection_transport_data_type_instance.to_dict()
# create an instance of BrokerConnectionTransportDataType from a dict
broker_connection_transport_data_type_from_dict = BrokerConnectionTransportDataType.from_dict(broker_connection_transport_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


