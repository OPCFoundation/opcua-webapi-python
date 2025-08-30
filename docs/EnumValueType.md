# EnumValueType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.2.12/#12.2.12.6).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] [default to 0]
**display_name** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.enum_value_type import EnumValueType

# TODO update the JSON string below
json = "{}"
# create an instance of EnumValueType from a JSON string
enum_value_type_instance = EnumValueType.from_json(json)
# print the JSON string representation of the object
print(EnumValueType.to_json())

# convert the object into a dict
enum_value_type_dict = enum_value_type_instance.to_dict()
# create an instance of EnumValueType from a dict
enum_value_type_from_dict = EnumValueType.from_dict(enum_value_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


