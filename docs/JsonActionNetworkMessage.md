# JsonActionNetworkMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**response_address** | **str** |  | [optional] 
**correlation_data** | **bytearray** |  | [optional] 
**requestor_id** | **str** |  | [optional] 
**timeout_hint** | **float** |  | [optional] [default to 0]
**messages** | **List[object]** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_action_network_message import JsonActionNetworkMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionNetworkMessage from a JSON string
json_action_network_message_instance = JsonActionNetworkMessage.from_json(json)
# print the JSON string representation of the object
print(JsonActionNetworkMessage.to_json())

# convert the object into a dict
json_action_network_message_dict = json_action_network_message_instance.to_dict()
# create an instance of JsonActionNetworkMessage from a dict
json_action_network_message_from_dict = JsonActionNetworkMessage.from_dict(json_action_network_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


