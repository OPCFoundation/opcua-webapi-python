# JsonWriterGroupMessageDataType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.3.2/#6.3.2.1.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_message_content_mask** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.json_writer_group_message_data_type import JsonWriterGroupMessageDataType

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWriterGroupMessageDataType from a JSON string
json_writer_group_message_data_type_instance = JsonWriterGroupMessageDataType.from_json(json)
# print the JSON string representation of the object
print(JsonWriterGroupMessageDataType.to_json())

# convert the object into a dict
json_writer_group_message_data_type_dict = json_writer_group_message_data_type_instance.to_dict()
# create an instance of JsonWriterGroupMessageDataType from a dict
json_writer_group_message_data_type_from_dict = JsonWriterGroupMessageDataType.from_dict(json_writer_group_message_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


