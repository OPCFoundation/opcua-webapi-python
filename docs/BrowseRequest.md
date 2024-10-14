# BrowseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**view** | [**ViewDescription**](ViewDescription.md) |  | [optional] 
**requested_max_references_per_node** | **int** |  | [optional] 
**nodes_to_browse** | [**List[BrowseDescription]**](BrowseDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_request import BrowseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseRequest from a JSON string
browse_request_instance = BrowseRequest.from_json(json)
# print the JSON string representation of the object
print(BrowseRequest.to_json())

# convert the object into a dict
browse_request_dict = browse_request_instance.to_dict()
# create an instance of BrowseRequest from a dict
browse_request_from_dict = BrowseRequest.from_dict(browse_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


