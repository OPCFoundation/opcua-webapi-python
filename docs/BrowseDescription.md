# BrowseDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**browse_direction** | **int** |  | [optional] 
**reference_type_id** | **str** |  | [optional] 
**include_subtypes** | **bool** |  | [optional] 
**node_class_mask** | **int** |  | [optional] 
**result_mask** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_description import BrowseDescription

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseDescription from a JSON string
browse_description_instance = BrowseDescription.from_json(json)
# print the JSON string representation of the object
print BrowseDescription.to_json()

# convert the object into a dict
browse_description_dict = browse_description_instance.to_dict()
# create an instance of BrowseDescription from a dict
browse_description_form_dict = browse_description.from_dict(browse_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


