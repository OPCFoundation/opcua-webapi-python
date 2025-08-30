# HistoryUpdateResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.5/#5.11.5.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[HistoryUpdateResult]**](HistoryUpdateResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_update_response import HistoryUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryUpdateResponse from a JSON string
history_update_response_instance = HistoryUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(HistoryUpdateResponse.to_json())

# convert the object into a dict
history_update_response_dict = history_update_response_instance.to_dict()
# create an instance of HistoryUpdateResponse from a dict
history_update_response_from_dict = HistoryUpdateResponse.from_dict(history_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


