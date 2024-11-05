# PubSubConnectionDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to False]
**publisher_id** | [**Variant**](Variant.md) |  | [optional] 
**transport_profile_uri** | **str** |  | [optional] 
**address** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**connection_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**transport_settings** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**writer_groups** | [**List[WriterGroupDataType]**](WriterGroupDataType.md) |  | [optional] 
**reader_groups** | [**List[ReaderGroupDataType]**](ReaderGroupDataType.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.pub_sub_connection_data_type import PubSubConnectionDataType

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubConnectionDataType from a JSON string
pub_sub_connection_data_type_instance = PubSubConnectionDataType.from_json(json)
# print the JSON string representation of the object
print(PubSubConnectionDataType.to_json())

# convert the object into a dict
pub_sub_connection_data_type_dict = pub_sub_connection_data_type_instance.to_dict()
# create an instance of PubSubConnectionDataType from a dict
pub_sub_connection_data_type_from_dict = PubSubConnectionDataType.from_dict(pub_sub_connection_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


