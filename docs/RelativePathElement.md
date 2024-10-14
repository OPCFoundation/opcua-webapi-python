# RelativePathElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_type_id** | **str** |  | [optional] 
**is_inverse** | **bool** |  | [optional] 
**include_subtypes** | **bool** |  | [optional] 
**target_name** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.relative_path_element import RelativePathElement

# TODO update the JSON string below
json = "{}"
# create an instance of RelativePathElement from a JSON string
relative_path_element_instance = RelativePathElement.from_json(json)
# print the JSON string representation of the object
print(RelativePathElement.to_json())

# convert the object into a dict
relative_path_element_dict = relative_path_element_instance.to_dict()
# create an instance of RelativePathElement from a dict
relative_path_element_from_dict = RelativePathElement.from_dict(relative_path_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


