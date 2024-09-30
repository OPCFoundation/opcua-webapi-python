# DataTypeSchemaHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespaces** | **List[str]** |  | [optional] 
**structure_data_types** | [**List[StructureDescription]**](StructureDescription.md) |  | [optional] 
**enum_data_types** | [**List[EnumDescription]**](EnumDescription.md) |  | [optional] 
**simple_data_types** | [**List[SimpleTypeDescription]**](SimpleTypeDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.data_type_schema_header import DataTypeSchemaHeader

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeSchemaHeader from a JSON string
data_type_schema_header_instance = DataTypeSchemaHeader.from_json(json)
# print the JSON string representation of the object
print DataTypeSchemaHeader.to_json()

# convert the object into a dict
data_type_schema_header_dict = data_type_schema_header_instance.to_dict()
# create an instance of DataTypeSchemaHeader from a dict
data_type_schema_header_form_dict = data_type_schema_header.from_dict(data_type_schema_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


