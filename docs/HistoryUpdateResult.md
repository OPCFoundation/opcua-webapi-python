# HistoryUpdateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**operation_results** | **List[int]** |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_update_result import HistoryUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryUpdateResult from a JSON string
history_update_result_instance = HistoryUpdateResult.from_json(json)
# print the JSON string representation of the object
print(HistoryUpdateResult.to_json())

# convert the object into a dict
history_update_result_dict = history_update_result_instance.to_dict()
# create an instance of HistoryUpdateResult from a dict
history_update_result_from_dict = HistoryUpdateResult.from_dict(history_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


