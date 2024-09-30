# PubSubGroupDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**security_mode** | **int** |  | [optional] 
**security_group_id** | **str** |  | [optional] 
**security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**max_network_message_size** | **int** |  | [optional] 
**group_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.pub_sub_group_data_type import PubSubGroupDataType

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubGroupDataType from a JSON string
pub_sub_group_data_type_instance = PubSubGroupDataType.from_json(json)
# print the JSON string representation of the object
print PubSubGroupDataType.to_json()

# convert the object into a dict
pub_sub_group_data_type_dict = pub_sub_group_data_type_instance.to_dict()
# create an instance of PubSubGroupDataType from a dict
pub_sub_group_data_type_form_dict = pub_sub_group_data_type.from_dict(pub_sub_group_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


