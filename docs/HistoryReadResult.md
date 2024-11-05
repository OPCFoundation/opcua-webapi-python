# HistoryReadResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 
**continuation_point** | **bytearray** |  | [optional] 
**history_data** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_read_result import HistoryReadResult

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryReadResult from a JSON string
history_read_result_instance = HistoryReadResult.from_json(json)
# print the JSON string representation of the object
print(HistoryReadResult.to_json())

# convert the object into a dict
history_read_result_dict = history_read_result_instance.to_dict()
# create an instance of HistoryReadResult from a dict
history_read_result_from_dict = HistoryReadResult.from_dict(history_read_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


