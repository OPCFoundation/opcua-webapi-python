# UnregisterNodesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.unregister_nodes_response import UnregisterNodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterNodesResponse from a JSON string
unregister_nodes_response_instance = UnregisterNodesResponse.from_json(json)
# print the JSON string representation of the object
print(UnregisterNodesResponse.to_json())

# convert the object into a dict
unregister_nodes_response_dict = unregister_nodes_response_instance.to_dict()
# create an instance of UnregisterNodesResponse from a dict
unregister_nodes_response_from_dict = UnregisterNodesResponse.from_dict(unregister_nodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


