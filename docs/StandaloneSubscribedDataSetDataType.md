# StandaloneSubscribedDataSetDataType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.10/#6.2.10.5).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_set_folder** | **List[str]** |  | [optional] 
**data_set_meta_data** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 
**subscribed_data_set** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.standalone_subscribed_data_set_data_type import StandaloneSubscribedDataSetDataType

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneSubscribedDataSetDataType from a JSON string
standalone_subscribed_data_set_data_type_instance = StandaloneSubscribedDataSetDataType.from_json(json)
# print the JSON string representation of the object
print(StandaloneSubscribedDataSetDataType.to_json())

# convert the object into a dict
standalone_subscribed_data_set_data_type_dict = standalone_subscribed_data_set_data_type_instance.to_dict()
# create an instance of StandaloneSubscribedDataSetDataType from a dict
standalone_subscribed_data_set_data_type_from_dict = StandaloneSubscribedDataSetDataType.from_dict(standalone_subscribed_data_set_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


