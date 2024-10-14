# TranslateBrowsePathsToNodeIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**browse_paths** | [**List[BrowsePath]**](BrowsePath.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.translate_browse_paths_to_node_ids_request import TranslateBrowsePathsToNodeIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateBrowsePathsToNodeIdsRequest from a JSON string
translate_browse_paths_to_node_ids_request_instance = TranslateBrowsePathsToNodeIdsRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateBrowsePathsToNodeIdsRequest.to_json())

# convert the object into a dict
translate_browse_paths_to_node_ids_request_dict = translate_browse_paths_to_node_ids_request_instance.to_dict()
# create an instance of TranslateBrowsePathsToNodeIdsRequest from a dict
translate_browse_paths_to_node_ids_request_from_dict = TranslateBrowsePathsToNodeIdsRequest.from_dict(translate_browse_paths_to_node_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


