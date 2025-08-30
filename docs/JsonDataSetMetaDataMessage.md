# JsonDataSetMetaDataMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**data_set_writer_id** | **int** |  | [optional] [default to 0]
**writer_group_name** | **str** |  | [optional] 
**data_set_writer_name** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**meta_data** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.json_data_set_meta_data_message import JsonDataSetMetaDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetMetaDataMessage from a JSON string
json_data_set_meta_data_message_instance = JsonDataSetMetaDataMessage.from_json(json)
# print the JSON string representation of the object
print(JsonDataSetMetaDataMessage.to_json())

# convert the object into a dict
json_data_set_meta_data_message_dict = json_data_set_meta_data_message_instance.to_dict()
# create an instance of JsonDataSetMetaDataMessage from a dict
json_data_set_meta_data_message_from_dict = JsonDataSetMetaDataMessage.from_dict(json_data_set_meta_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


