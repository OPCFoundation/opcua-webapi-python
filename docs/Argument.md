# Argument

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.2.12/#12.2.12.1).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**value_rank** | **int** |  | [optional] [default to 0]
**array_dimensions** | **List[int]** |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.argument import Argument

# TODO update the JSON string below
json = "{}"
# create an instance of Argument from a JSON string
argument_instance = Argument.from_json(json)
# print the JSON string representation of the object
print(Argument.to_json())

# convert the object into a dict
argument_dict = argument_instance.to_dict()
# create an instance of Argument from a dict
argument_from_dict = Argument.from_dict(argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


