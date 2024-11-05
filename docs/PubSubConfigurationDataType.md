# PubSubConfigurationDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published_data_sets** | [**List[PublishedDataSetDataType]**](PublishedDataSetDataType.md) |  | [optional] 
**connections** | [**List[PubSubConnectionDataType]**](PubSubConnectionDataType.md) |  | [optional] 
**enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from opcua_webapi.models.pub_sub_configuration_data_type import PubSubConfigurationDataType

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubConfigurationDataType from a JSON string
pub_sub_configuration_data_type_instance = PubSubConfigurationDataType.from_json(json)
# print the JSON string representation of the object
print(PubSubConfigurationDataType.to_json())

# convert the object into a dict
pub_sub_configuration_data_type_dict = pub_sub_configuration_data_type_instance.to_dict()
# create an instance of PubSubConfigurationDataType from a dict
pub_sub_configuration_data_type_from_dict = PubSubConfigurationDataType.from_dict(pub_sub_configuration_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


