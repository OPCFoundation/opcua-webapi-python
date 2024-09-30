# StandaloneSubscribedDataSetDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_set_folder** | **List[str]** |  | [optional] 
**data_set_meta_data** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 
**subscribed_data_set** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.standalone_subscribed_data_set_data_type import StandaloneSubscribedDataSetDataType

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneSubscribedDataSetDataType from a JSON string
standalone_subscribed_data_set_data_type_instance = StandaloneSubscribedDataSetDataType.from_json(json)
# print the JSON string representation of the object
print StandaloneSubscribedDataSetDataType.to_json()

# convert the object into a dict
standalone_subscribed_data_set_data_type_dict = standalone_subscribed_data_set_data_type_instance.to_dict()
# create an instance of StandaloneSubscribedDataSetDataType from a dict
standalone_subscribed_data_set_data_type_form_dict = standalone_subscribed_data_set_data_type.from_dict(standalone_subscribed_data_set_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


