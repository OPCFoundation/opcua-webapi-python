# DataSetReaderDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**publisher_id** | [**Variant**](Variant.md) |  | [optional] 
**writer_group_id** | **int** |  | [optional] 
**data_set_writer_id** | **int** |  | [optional] 
**data_set_meta_data** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 
**data_set_field_content_mask** | **int** |  | [optional] 
**message_receive_timeout** | **float** |  | [optional] 
**key_frame_count** | **int** |  | [optional] 
**header_layout_uri** | **str** |  | [optional] 
**security_mode** | **int** |  | [optional] 
**security_group_id** | **str** |  | [optional] 
**security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**data_set_reader_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**transport_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**message_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**subscribed_data_set** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.data_set_reader_data_type import DataSetReaderDataType

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetReaderDataType from a JSON string
data_set_reader_data_type_instance = DataSetReaderDataType.from_json(json)
# print the JSON string representation of the object
print DataSetReaderDataType.to_json()

# convert the object into a dict
data_set_reader_data_type_dict = data_set_reader_data_type_instance.to_dict()
# create an instance of DataSetReaderDataType from a dict
data_set_reader_data_type_form_dict = data_set_reader_data_type.from_dict(data_set_reader_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


