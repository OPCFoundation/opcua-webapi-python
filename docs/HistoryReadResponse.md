# HistoryReadResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.3/#5.11.3.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[HistoryReadResult]**](HistoryReadResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_read_response import HistoryReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryReadResponse from a JSON string
history_read_response_instance = HistoryReadResponse.from_json(json)
# print the JSON string representation of the object
print(HistoryReadResponse.to_json())

# convert the object into a dict
history_read_response_dict = history_read_response_instance.to_dict()
# create an instance of HistoryReadResponse from a dict
history_read_response_from_dict = HistoryReadResponse.from_dict(history_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


