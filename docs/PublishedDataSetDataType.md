# PublishedDataSetDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_set_folder** | **List[str]** |  | [optional] 
**data_set_meta_data** | [**DataSetMetaDataType**](DataSetMetaDataType.md) |  | [optional] 
**extension_fields** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**data_set_source** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.published_data_set_data_type import PublishedDataSetDataType

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedDataSetDataType from a JSON string
published_data_set_data_type_instance = PublishedDataSetDataType.from_json(json)
# print the JSON string representation of the object
print PublishedDataSetDataType.to_json()

# convert the object into a dict
published_data_set_data_type_dict = published_data_set_data_type_instance.to_dict()
# create an instance of PublishedDataSetDataType from a dict
published_data_set_data_type_form_dict = published_data_set_data_type.from_dict(published_data_set_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


