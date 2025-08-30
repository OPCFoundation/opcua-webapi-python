# ActionTargetDataType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.3/#6.2.3.10.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_target_id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.action_target_data_type import ActionTargetDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTargetDataType from a JSON string
action_target_data_type_instance = ActionTargetDataType.from_json(json)
# print the JSON string representation of the object
print(ActionTargetDataType.to_json())

# convert the object into a dict
action_target_data_type_dict = action_target_data_type_instance.to_dict()
# create an instance of ActionTargetDataType from a dict
action_target_data_type_from_dict = ActionTargetDataType.from_dict(action_target_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


