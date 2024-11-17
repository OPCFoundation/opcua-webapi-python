# ActionMethodDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** |  | [optional] 
**method_id** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.action_method_data_type import ActionMethodDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ActionMethodDataType from a JSON string
action_method_data_type_instance = ActionMethodDataType.from_json(json)
# print the JSON string representation of the object
print(ActionMethodDataType.to_json())

# convert the object into a dict
action_method_data_type_dict = action_method_data_type_instance.to_dict()
# create an instance of ActionMethodDataType from a dict
action_method_data_type_from_dict = ActionMethodDataType.from_dict(action_method_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


