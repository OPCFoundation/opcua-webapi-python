# WriterGroupDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**writer_group_id** | **int** |  | [optional] 
**publishing_interval** | **float** |  | [optional] 
**keep_alive_time** | **float** |  | [optional] 
**priority** | **int** |  | [optional] 
**locale_ids** | **List[str]** |  | [optional] 
**header_layout_uri** | **str** |  | [optional] 
**transport_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**message_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**data_set_writers** | [**List[DataSetWriterDataType]**](DataSetWriterDataType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**security_mode** | **int** |  | [optional] 
**security_group_id** | **str** |  | [optional] 
**security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**max_network_message_size** | **int** |  | [optional] 
**group_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.writer_group_data_type import WriterGroupDataType

# TODO update the JSON string below
json = "{}"
# create an instance of WriterGroupDataType from a JSON string
writer_group_data_type_instance = WriterGroupDataType.from_json(json)
# print the JSON string representation of the object
print(WriterGroupDataType.to_json())

# convert the object into a dict
writer_group_data_type_dict = writer_group_data_type_instance.to_dict()
# create an instance of WriterGroupDataType from a dict
writer_group_data_type_from_dict = WriterGroupDataType.from_dict(writer_group_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


