# EnumDescription

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.34).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum_definition** | [**EnumDefinition**](EnumDefinition.md) |  | [optional] 
**built_in_type** | **int** |  | [optional] [default to 0]
**data_type_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.enum_description import EnumDescription

# TODO update the JSON string below
json = "{}"
# create an instance of EnumDescription from a JSON string
enum_description_instance = EnumDescription.from_json(json)
# print the JSON string representation of the object
print(EnumDescription.to_json())

# convert the object into a dict
enum_description_dict = enum_description_instance.to_dict()
# create an instance of EnumDescription from a dict
enum_description_from_dict = EnumDescription.from_dict(enum_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


