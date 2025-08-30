# SimpleTypeDescription

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.35).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_data_type** | **str** |  | [optional] 
**built_in_type** | **int** |  | [optional] [default to 0]
**data_type_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.simple_type_description import SimpleTypeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTypeDescription from a JSON string
simple_type_description_instance = SimpleTypeDescription.from_json(json)
# print the JSON string representation of the object
print(SimpleTypeDescription.to_json())

# convert the object into a dict
simple_type_description_dict = simple_type_description_instance.to_dict()
# create an instance of SimpleTypeDescription from a dict
simple_type_description_from_dict = SimpleTypeDescription.from_dict(simple_type_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


