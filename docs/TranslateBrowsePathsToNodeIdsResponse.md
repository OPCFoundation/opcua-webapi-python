# TranslateBrowsePathsToNodeIdsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[BrowsePathResult]**](BrowsePathResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.translate_browse_paths_to_node_ids_response import TranslateBrowsePathsToNodeIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateBrowsePathsToNodeIdsResponse from a JSON string
translate_browse_paths_to_node_ids_response_instance = TranslateBrowsePathsToNodeIdsResponse.from_json(json)
# print the JSON string representation of the object
print TranslateBrowsePathsToNodeIdsResponse.to_json()

# convert the object into a dict
translate_browse_paths_to_node_ids_response_dict = translate_browse_paths_to_node_ids_response_instance.to_dict()
# create an instance of TranslateBrowsePathsToNodeIdsResponse from a dict
translate_browse_paths_to_node_ids_response_form_dict = translate_browse_paths_to_node_ids_response.from_dict(translate_browse_paths_to_node_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


