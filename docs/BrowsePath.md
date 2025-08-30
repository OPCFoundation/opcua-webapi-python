# BrowsePath

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part3/6.2.5).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starting_node** | **str** |  | [optional] 
**relative_path** | [**RelativePath**](RelativePath.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_path import BrowsePath

# TODO update the JSON string below
json = "{}"
# create an instance of BrowsePath from a JSON string
browse_path_instance = BrowsePath.from_json(json)
# print the JSON string representation of the object
print(BrowsePath.to_json())

# convert the object into a dict
browse_path_dict = browse_path_instance.to_dict()
# create an instance of BrowsePath from a dict
browse_path_from_dict = BrowsePath.from_dict(browse_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


