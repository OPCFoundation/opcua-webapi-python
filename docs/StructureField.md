# StructureField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**data_type** | **str** |  | [optional] 
**value_rank** | **int** |  | [optional] 
**array_dimensions** | **List[int]** |  | [optional] 
**max_string_length** | **int** |  | [optional] 
**is_optional** | **bool** |  | [optional] 

## Example

```python
from opcua_webapi.models.structure_field import StructureField

# TODO update the JSON string below
json = "{}"
# create an instance of StructureField from a JSON string
structure_field_instance = StructureField.from_json(json)
# print the JSON string representation of the object
print StructureField.to_json()

# convert the object into a dict
structure_field_dict = structure_field_instance.to_dict()
# create an instance of StructureField from a dict
structure_field_form_dict = structure_field.from_dict(structure_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


