# RegisterNodesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**registered_node_ids** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.register_nodes_response import RegisterNodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterNodesResponse from a JSON string
register_nodes_response_instance = RegisterNodesResponse.from_json(json)
# print the JSON string representation of the object
print RegisterNodesResponse.to_json()

# convert the object into a dict
register_nodes_response_dict = register_nodes_response_instance.to_dict()
# create an instance of RegisterNodesResponse from a dict
register_nodes_response_form_dict = register_nodes_response.from_dict(register_nodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


