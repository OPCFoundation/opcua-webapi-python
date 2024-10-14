# CallMethodResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**input_argument_results** | **List[int]** |  | [optional] 
**input_argument_diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 
**output_arguments** | [**List[Variant]**](Variant.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.call_method_result import CallMethodResult

# TODO update the JSON string below
json = "{}"
# create an instance of CallMethodResult from a JSON string
call_method_result_instance = CallMethodResult.from_json(json)
# print the JSON string representation of the object
print(CallMethodResult.to_json())

# convert the object into a dict
call_method_result_dict = call_method_result_instance.to_dict()
# create an instance of CallMethodResult from a dict
call_method_result_from_dict = CallMethodResult.from_dict(call_method_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


