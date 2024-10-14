# StructureDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structure_definition** | [**StructureDefinition**](StructureDefinition.md) |  | [optional] 
**data_type_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.structure_description import StructureDescription

# TODO update the JSON string below
json = "{}"
# create an instance of StructureDescription from a JSON string
structure_description_instance = StructureDescription.from_json(json)
# print the JSON string representation of the object
print(StructureDescription.to_json())

# convert the object into a dict
structure_description_dict = structure_description_instance.to_dict()
# create an instance of StructureDescription from a dict
structure_description_from_dict = StructureDescription.from_dict(structure_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


