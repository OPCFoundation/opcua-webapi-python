# JsonServerEndpointsMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | [**ApplicationDescription**](ApplicationDescription.md) |  | [optional] 
**endpoints** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.json_server_endpoints_message import JsonServerEndpointsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonServerEndpointsMessage from a JSON string
json_server_endpoints_message_instance = JsonServerEndpointsMessage.from_json(json)
# print the JSON string representation of the object
print(JsonServerEndpointsMessage.to_json())

# convert the object into a dict
json_server_endpoints_message_dict = json_server_endpoints_message_instance.to_dict()
# create an instance of JsonServerEndpointsMessage from a dict
json_server_endpoints_message_from_dict = JsonServerEndpointsMessage.from_dict(json_server_endpoints_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


