# WriteValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**attribute_id** | **int** |  | [optional] 
**index_range** | **str** |  | [optional] 
**value** | [**DataValue**](DataValue.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.write_value import WriteValue

# TODO update the JSON string below
json = "{}"
# create an instance of WriteValue from a JSON string
write_value_instance = WriteValue.from_json(json)
# print the JSON string representation of the object
print WriteValue.to_json()

# convert the object into a dict
write_value_dict = write_value_instance.to_dict()
# create an instance of WriteValue from a dict
write_value_form_dict = write_value.from_dict(write_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


