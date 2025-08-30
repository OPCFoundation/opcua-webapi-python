# JsonDataSetMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_writer_id** | **int** |  | [optional] [default to 0]
**data_set_writer_name** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**writer_group_name** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] [default to 0]
**meta_data_version** | [**ConfigurationVersionDataType**](ConfigurationVersionDataType.md) |  | [optional] 
**minor_version** | **int** |  | [optional] [default to 0]
**timestamp** | **datetime** |  | [optional] 
**status** | [**StatusCode**](StatusCode.md) |  | [optional] 
**message_type** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_data_set_message import JsonDataSetMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetMessage from a JSON string
json_data_set_message_instance = JsonDataSetMessage.from_json(json)
# print the JSON string representation of the object
print(JsonDataSetMessage.to_json())

# convert the object into a dict
json_data_set_message_dict = json_data_set_message_instance.to_dict()
# create an instance of JsonDataSetMessage from a dict
json_data_set_message_from_dict = JsonDataSetMessage.from_dict(json_data_set_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


