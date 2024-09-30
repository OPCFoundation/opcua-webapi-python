# RegisterNodesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**nodes_to_register** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.register_nodes_request import RegisterNodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterNodesRequest from a JSON string
register_nodes_request_instance = RegisterNodesRequest.from_json(json)
# print the JSON string representation of the object
print RegisterNodesRequest.to_json()

# convert the object into a dict
register_nodes_request_dict = register_nodes_request_instance.to_dict()
# create an instance of RegisterNodesRequest from a dict
register_nodes_request_form_dict = register_nodes_request.from_dict(register_nodes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


