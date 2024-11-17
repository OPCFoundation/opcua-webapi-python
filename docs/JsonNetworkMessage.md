# JsonNetworkMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**writer_group_name** | **str** |  | [optional] 
**data_set_class_id** | **str** |  | [optional] 
**messages** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_network_message import JsonNetworkMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonNetworkMessage from a JSON string
json_network_message_instance = JsonNetworkMessage.from_json(json)
# print the JSON string representation of the object
print(JsonNetworkMessage.to_json())

# convert the object into a dict
json_network_message_dict = json_network_message_instance.to_dict()
# create an instance of JsonNetworkMessage from a dict
json_network_message_from_dict = JsonNetworkMessage.from_dict(json_network_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


