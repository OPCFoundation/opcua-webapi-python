# FieldMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**field_flags** | **int** |  | [optional] [default to 0]
**built_in_type** | **int** |  | [optional] [default to 0]
**data_type** | **str** |  | [optional] 
**value_rank** | **int** |  | [optional] [default to 0]
**array_dimensions** | **List[int]** |  | [optional] 
**max_string_length** | **int** |  | [optional] [default to 0]
**data_set_field_id** | **str** |  | [optional] 
**properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.field_meta_data import FieldMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of FieldMetaData from a JSON string
field_meta_data_instance = FieldMetaData.from_json(json)
# print the JSON string representation of the object
print(FieldMetaData.to_json())

# convert the object into a dict
field_meta_data_dict = field_meta_data_instance.to_dict()
# create an instance of FieldMetaData from a dict
field_meta_data_from_dict = FieldMetaData.from_dict(field_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


