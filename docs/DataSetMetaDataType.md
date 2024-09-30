# DataSetMetaDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**fields** | [**List[FieldMetaData]**](FieldMetaData.md) |  | [optional] 
**data_set_class_id** | **str** |  | [optional] 
**configuration_version** | [**ConfigurationVersionDataType**](ConfigurationVersionDataType.md) |  | [optional] 
**namespaces** | **List[str]** |  | [optional] 
**structure_data_types** | [**List[StructureDescription]**](StructureDescription.md) |  | [optional] 
**enum_data_types** | [**List[EnumDescription]**](EnumDescription.md) |  | [optional] 
**simple_data_types** | [**List[SimpleTypeDescription]**](SimpleTypeDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.data_set_meta_data_type import DataSetMetaDataType

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetMetaDataType from a JSON string
data_set_meta_data_type_instance = DataSetMetaDataType.from_json(json)
# print the JSON string representation of the object
print DataSetMetaDataType.to_json()

# convert the object into a dict
data_set_meta_data_type_dict = data_set_meta_data_type_instance.to_dict()
# create an instance of DataSetMetaDataType from a dict
data_set_meta_data_type_form_dict = data_set_meta_data_type.from_dict(data_set_meta_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


