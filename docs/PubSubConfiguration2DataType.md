# PubSubConfiguration2DataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribed_data_sets** | [**List[StandaloneSubscribedDataSetDataType]**](StandaloneSubscribedDataSetDataType.md) |  | [optional] 
**data_set_classes** | [**List[DataSetMetaDataType]**](DataSetMetaDataType.md) |  | [optional] 
**default_security_key_services** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**security_groups** | [**List[SecurityGroupDataType]**](SecurityGroupDataType.md) |  | [optional] 
**pub_sub_key_push_targets** | [**List[PubSubKeyPushTargetDataType]**](PubSubKeyPushTargetDataType.md) |  | [optional] 
**configuration_version** | **int** |  | [optional] 
**configuration_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**published_data_sets** | [**List[PublishedDataSetDataType]**](PublishedDataSetDataType.md) |  | [optional] 
**connections** | [**List[PubSubConnectionDataType]**](PubSubConnectionDataType.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from opcua_webapi.models.pub_sub_configuration2_data_type import PubSubConfiguration2DataType

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubConfiguration2DataType from a JSON string
pub_sub_configuration2_data_type_instance = PubSubConfiguration2DataType.from_json(json)
# print the JSON string representation of the object
print(PubSubConfiguration2DataType.to_json())

# convert the object into a dict
pub_sub_configuration2_data_type_dict = pub_sub_configuration2_data_type_instance.to_dict()
# create an instance of PubSubConfiguration2DataType from a dict
pub_sub_configuration2_data_type_from_dict = PubSubConfiguration2DataType.from_dict(pub_sub_configuration2_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


