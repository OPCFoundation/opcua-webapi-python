# HistoryReadValueId

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.3/#5.11.3.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**index_range** | **str** |  | [optional] 
**data_encoding** | **str** |  | [optional] 
**continuation_point** | **bytearray** |  | [optional] 

## Example

```python
from opcua_webapi.models.history_read_value_id import HistoryReadValueId

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryReadValueId from a JSON string
history_read_value_id_instance = HistoryReadValueId.from_json(json)
# print the JSON string representation of the object
print(HistoryReadValueId.to_json())

# convert the object into a dict
history_read_value_id_dict = history_read_value_id_instance.to_dict()
# create an instance of HistoryReadValueId from a dict
history_read_value_id_from_dict = HistoryReadValueId.from_dict(history_read_value_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


