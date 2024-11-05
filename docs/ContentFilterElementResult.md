# ContentFilterElementResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 
**operand_status_codes** | [**List[StatusCode]**](StatusCode.md) |  | [optional] 
**operand_diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.content_filter_element_result import ContentFilterElementResult

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFilterElementResult from a JSON string
content_filter_element_result_instance = ContentFilterElementResult.from_json(json)
# print the JSON string representation of the object
print(ContentFilterElementResult.to_json())

# convert the object into a dict
content_filter_element_result_dict = content_filter_element_result_instance.to_dict()
# create an instance of ContentFilterElementResult from a dict
content_filter_element_result_from_dict = ContentFilterElementResult.from_dict(content_filter_element_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


