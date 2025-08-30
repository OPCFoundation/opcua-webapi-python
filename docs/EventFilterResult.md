# EventFilterResult

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.22.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_clause_results** | [**List[StatusCode]**](StatusCode.md) |  | [optional] 
**select_clause_diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 
**where_clause_result** | [**ContentFilterResult**](ContentFilterResult.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.event_filter_result import EventFilterResult

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilterResult from a JSON string
event_filter_result_instance = EventFilterResult.from_json(json)
# print the JSON string representation of the object
print(EventFilterResult.to_json())

# convert the object into a dict
event_filter_result_dict = event_filter_result_instance.to_dict()
# create an instance of EventFilterResult from a dict
event_filter_result_from_dict = EventFilterResult.from_dict(event_filter_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


