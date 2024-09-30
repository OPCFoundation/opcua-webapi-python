# ReadValueId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**attribute_id** | **int** |  | [optional] 
**index_range** | **str** |  | [optional] 
**data_encoding** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.read_value_id import ReadValueId

# TODO update the JSON string below
json = "{}"
# create an instance of ReadValueId from a JSON string
read_value_id_instance = ReadValueId.from_json(json)
# print the JSON string representation of the object
print ReadValueId.to_json()

# convert the object into a dict
read_value_id_dict = read_value_id_instance.to_dict()
# create an instance of ReadValueId from a dict
read_value_id_form_dict = read_value_id.from_dict(read_value_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


