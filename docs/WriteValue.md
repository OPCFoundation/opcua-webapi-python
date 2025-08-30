# WriteValue

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.4/#5.11.4.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**attribute_id** | **int** |  | [optional] [default to 0]
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
print(WriteValue.to_json())

# convert the object into a dict
write_value_dict = write_value_instance.to_dict()
# create an instance of WriteValue from a dict
write_value_from_dict = WriteValue.from_dict(write_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


