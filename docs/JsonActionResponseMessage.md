# JsonActionResponseMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_writer_id** | **int** |  | [optional] [default to 0]
**action_target_id** | **int** |  | [optional] [default to 0]
**data_set_writer_name** | **str** |  | [optional] 
**writer_group_name** | **str** |  | [optional] 
**meta_data_version** | [**ConfigurationVersionDataType**](ConfigurationVersionDataType.md) |  | [optional] 
**minor_version** | **int** |  | [optional] [default to 0]
**timestamp** | **datetime** |  | [optional] 
**status** | [**StatusCode**](StatusCode.md) |  | [optional] 
**message_type** | **str** |  | [optional] 
**request_id** | **int** |  | [optional] [default to 0]
**action_state** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.11/#6.2.11.2.1). | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_action_response_message import JsonActionResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionResponseMessage from a JSON string
json_action_response_message_instance = JsonActionResponseMessage.from_json(json)
# print the JSON string representation of the object
print(JsonActionResponseMessage.to_json())

# convert the object into a dict
json_action_response_message_dict = json_action_response_message_instance.to_dict()
# create an instance of JsonActionResponseMessage from a dict
json_action_response_message_from_dict = JsonActionResponseMessage.from_dict(json_action_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


