# ContentFilterResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_results** | [**List[ContentFilterElementResult]**](ContentFilterElementResult.md) |  | [optional] 
**element_diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.content_filter_result import ContentFilterResult

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFilterResult from a JSON string
content_filter_result_instance = ContentFilterResult.from_json(json)
# print the JSON string representation of the object
print ContentFilterResult.to_json()

# convert the object into a dict
content_filter_result_dict = content_filter_result_instance.to_dict()
# create an instance of ContentFilterResult from a dict
content_filter_result_form_dict = content_filter_result.from_dict(content_filter_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


