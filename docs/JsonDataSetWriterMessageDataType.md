# JsonDataSetWriterMessageDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_message_content_mask** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_data_set_writer_message_data_type import JsonDataSetWriterMessageDataType

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetWriterMessageDataType from a JSON string
json_data_set_writer_message_data_type_instance = JsonDataSetWriterMessageDataType.from_json(json)
# print the JSON string representation of the object
print JsonDataSetWriterMessageDataType.to_json()

# convert the object into a dict
json_data_set_writer_message_data_type_dict = json_data_set_writer_message_data_type_instance.to_dict()
# create an instance of JsonDataSetWriterMessageDataType from a dict
json_data_set_writer_message_data_type_form_dict = json_data_set_writer_message_data_type.from_dict(json_data_set_writer_message_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


