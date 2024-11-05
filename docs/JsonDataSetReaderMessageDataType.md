# JsonDataSetReaderMessageDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_message_content_mask** | **int** |  | [optional] [default to 0]
**data_set_message_content_mask** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.json_data_set_reader_message_data_type import JsonDataSetReaderMessageDataType

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetReaderMessageDataType from a JSON string
json_data_set_reader_message_data_type_instance = JsonDataSetReaderMessageDataType.from_json(json)
# print the JSON string representation of the object
print(JsonDataSetReaderMessageDataType.to_json())

# convert the object into a dict
json_data_set_reader_message_data_type_dict = json_data_set_reader_message_data_type_instance.to_dict()
# create an instance of JsonDataSetReaderMessageDataType from a dict
json_data_set_reader_message_data_type_from_dict = JsonDataSetReaderMessageDataType.from_dict(json_data_set_reader_message_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


