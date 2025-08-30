# JsonActionResponderMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**connection** | [**PubSubConnectionDataType**](PubSubConnectionDataType.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.json_action_responder_message import JsonActionResponderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionResponderMessage from a JSON string
json_action_responder_message_instance = JsonActionResponderMessage.from_json(json)
# print the JSON string representation of the object
print(JsonActionResponderMessage.to_json())

# convert the object into a dict
json_action_responder_message_dict = json_action_responder_message_instance.to_dict()
# create an instance of JsonActionResponderMessage from a dict
json_action_responder_message_from_dict = JsonActionResponderMessage.from_dict(json_action_responder_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


