# PubSubGroupDataType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.5/#6.2.5.7).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to False]
**security_mode** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.3.10). | [optional] 
**security_group_id** | **str** |  | [optional] 
**security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**max_network_message_size** | **int** |  | [optional] [default to 0]
**group_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.pub_sub_group_data_type import PubSubGroupDataType

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubGroupDataType from a JSON string
pub_sub_group_data_type_instance = PubSubGroupDataType.from_json(json)
# print the JSON string representation of the object
print(PubSubGroupDataType.to_json())

# convert the object into a dict
pub_sub_group_data_type_dict = pub_sub_group_data_type_instance.to_dict()
# create an instance of PubSubGroupDataType from a dict
pub_sub_group_data_type_from_dict = PubSubGroupDataType.from_dict(pub_sub_group_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


