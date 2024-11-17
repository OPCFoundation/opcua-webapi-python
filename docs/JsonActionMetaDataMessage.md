# JsonActionMetaDataMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**data_set_writer_id** | **int** |  | [optional] [default to 0]
**data_set_writer_name** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**action_targets** | [**List[ActionTargetDataType]**](ActionTargetDataType.md) |  | [optional] 
**request** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 
**response** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 
**action_methods** | [**List[ActionMethodDataType]**](ActionMethodDataType.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.json_action_meta_data_message import JsonActionMetaDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonActionMetaDataMessage from a JSON string
json_action_meta_data_message_instance = JsonActionMetaDataMessage.from_json(json)
# print the JSON string representation of the object
print(JsonActionMetaDataMessage.to_json())

# convert the object into a dict
json_action_meta_data_message_dict = json_action_meta_data_message_instance.to_dict()
# create an instance of JsonActionMetaDataMessage from a dict
json_action_meta_data_message_from_dict = JsonActionMetaDataMessage.from_dict(json_action_meta_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


