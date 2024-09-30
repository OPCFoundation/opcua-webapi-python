# EnumDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[EnumField]**](EnumField.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.enum_definition import EnumDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of EnumDefinition from a JSON string
enum_definition_instance = EnumDefinition.from_json(json)
# print the JSON string representation of the object
print EnumDefinition.to_json()

# convert the object into a dict
enum_definition_dict = enum_definition_instance.to_dict()
# create an instance of EnumDefinition from a dict
enum_definition_form_dict = enum_definition.from_dict(enum_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


