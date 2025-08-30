# ReaderGroupDataType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.8/#6.2.8.2.1).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_settings** | **object** |  | [optional] 
**message_settings** | **object** |  | [optional] 
**data_set_readers** | [**List[DataSetReaderDataType]**](DataSetReaderDataType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to False]
**security_mode** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.3.10). | [optional] 
**security_group_id** | **str** |  | [optional] 
**security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**max_network_message_size** | **int** |  | [optional] [default to 0]
**group_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.reader_group_data_type import ReaderGroupDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ReaderGroupDataType from a JSON string
reader_group_data_type_instance = ReaderGroupDataType.from_json(json)
# print the JSON string representation of the object
print(ReaderGroupDataType.to_json())

# convert the object into a dict
reader_group_data_type_dict = reader_group_data_type_instance.to_dict()
# create an instance of ReaderGroupDataType from a dict
reader_group_data_type_from_dict = ReaderGroupDataType.from_dict(reader_group_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


