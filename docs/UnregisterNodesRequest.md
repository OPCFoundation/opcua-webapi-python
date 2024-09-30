# UnregisterNodesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**nodes_to_unregister** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.unregister_nodes_request import UnregisterNodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterNodesRequest from a JSON string
unregister_nodes_request_instance = UnregisterNodesRequest.from_json(json)
# print the JSON string representation of the object
print UnregisterNodesRequest.to_json()

# convert the object into a dict
unregister_nodes_request_dict = unregister_nodes_request_instance.to_dict()
# create an instance of UnregisterNodesRequest from a dict
unregister_nodes_request_form_dict = unregister_nodes_request.from_dict(unregister_nodes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


