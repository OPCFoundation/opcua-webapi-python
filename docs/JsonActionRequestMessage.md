# JsonActionRequestMessage


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
**message_type** | **str** |  | [optional] 
**request_id** | **int** |  | [optional] [default to 0]
**action_state** | **int** |  | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_action_request_message import JsonActionRequestMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionRequestMessage from a JSON string
json_action_request_message_instance = JsonActionRequestMessage.from_json(json)
# print the JSON string representation of the object
print(JsonActionRequestMessage.to_json())

# convert the object into a dict
json_action_request_message_dict = json_action_request_message_instance.to_dict()
# create an instance of JsonActionRequestMessage from a dict
json_action_request_message_from_dict = JsonActionRequestMessage.from_dict(json_action_request_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


