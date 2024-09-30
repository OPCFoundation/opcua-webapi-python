# NetworkAddressDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_interface** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.network_address_data_type import NetworkAddressDataType

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressDataType from a JSON string
network_address_data_type_instance = NetworkAddressDataType.from_json(json)
# print the JSON string representation of the object
print NetworkAddressDataType.to_json()

# convert the object into a dict
network_address_data_type_dict = network_address_data_type_instance.to_dict()
# create an instance of NetworkAddressDataType from a dict
network_address_data_type_form_dict = network_address_data_type.from_dict(network_address_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


