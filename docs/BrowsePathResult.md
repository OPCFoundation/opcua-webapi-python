# BrowsePathResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**targets** | [**List[BrowsePathTarget]**](BrowsePathTarget.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_path_result import BrowsePathResult

# TODO update the JSON string below
json = "{}"
# create an instance of BrowsePathResult from a JSON string
browse_path_result_instance = BrowsePathResult.from_json(json)
# print the JSON string representation of the object
print BrowsePathResult.to_json()

# convert the object into a dict
browse_path_result_dict = browse_path_result_instance.to_dict()
# create an instance of BrowsePathResult from a dict
browse_path_result_form_dict = browse_path_result.from_dict(browse_path_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


