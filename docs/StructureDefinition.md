# StructureDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_encoding_id** | **str** |  | [optional] 
**base_data_type** | **str** |  | [optional] 
**structure_type** | **int** |  | [optional] 
**fields** | [**List[StructureField]**](StructureField.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.structure_definition import StructureDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StructureDefinition from a JSON string
structure_definition_instance = StructureDefinition.from_json(json)
# print the JSON string representation of the object
print(StructureDefinition.to_json())

# convert the object into a dict
structure_definition_dict = structure_definition_instance.to_dict()
# create an instance of StructureDefinition from a dict
structure_definition_from_dict = StructureDefinition.from_dict(structure_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


