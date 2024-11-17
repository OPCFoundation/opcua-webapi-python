# JsonPubSubConnectionMessage


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
from opcua_webapi.models.json_pub_sub_connection_message import JsonPubSubConnectionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPubSubConnectionMessage from a JSON string
json_pub_sub_connection_message_instance = JsonPubSubConnectionMessage.from_json(json)
# print the JSON string representation of the object
print(JsonPubSubConnectionMessage.to_json())

# convert the object into a dict
json_pub_sub_connection_message_dict = json_pub_sub_connection_message_instance.to_dict()
# create an instance of JsonPubSubConnectionMessage from a dict
json_pub_sub_connection_message_from_dict = JsonPubSubConnectionMessage.from_dict(json_pub_sub_connection_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


