# BrowsePathTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** |  | [optional] 
**remaining_path_index** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.browse_path_target import BrowsePathTarget

# TODO update the JSON string below
json = "{}"
# create an instance of BrowsePathTarget from a JSON string
browse_path_target_instance = BrowsePathTarget.from_json(json)
# print the JSON string representation of the object
print(BrowsePathTarget.to_json())

# convert the object into a dict
browse_path_target_dict = browse_path_target_instance.to_dict()
# create an instance of BrowsePathTarget from a dict
browse_path_target_from_dict = BrowsePathTarget.from_dict(browse_path_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


