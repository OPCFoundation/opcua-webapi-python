# ReaderGroupDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**message_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**data_set_readers** | [**List[DataSetReaderDataType]**](DataSetReaderDataType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**security_mode** | **int** |  | [optional] 
**security_group_id** | **str** |  | [optional] 
**security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**max_network_message_size** | **int** |  | [optional] 
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


