# DataSetWriterDataType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.4/#6.2.4.5.1).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to False]
**data_set_writer_id** | **int** |  | [optional] [default to 0]
**data_set_field_content_mask** | **int** |  | [optional] [default to 0]
**key_frame_count** | **int** |  | [optional] [default to 0]
**data_set_name** | **str** |  | [optional] 
**data_set_writer_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**transport_settings** | **object** |  | [optional] 
**message_settings** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.data_set_writer_data_type import DataSetWriterDataType

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetWriterDataType from a JSON string
data_set_writer_data_type_instance = DataSetWriterDataType.from_json(json)
# print the JSON string representation of the object
print(DataSetWriterDataType.to_json())

# convert the object into a dict
data_set_writer_data_type_dict = data_set_writer_data_type_instance.to_dict()
# create an instance of DataSetWriterDataType from a dict
data_set_writer_data_type_from_dict = DataSetWriterDataType.from_dict(data_set_writer_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


