# EnumField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **int** |  | [optional] [default to 0]
**display_name** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.enum_field import EnumField

# TODO update the JSON string below
json = "{}"
# create an instance of EnumField from a JSON string
enum_field_instance = EnumField.from_json(json)
# print the JSON string representation of the object
print(EnumField.to_json())

# convert the object into a dict
enum_field_dict = enum_field_instance.to_dict()
# create an instance of EnumField from a dict
enum_field_from_dict = EnumField.from_dict(enum_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


