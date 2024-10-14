# DiagnosticInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbolic_id** | **int** |  | [optional] 
**namespace_uri** | **int** |  | [optional] 
**locale** | **int** |  | [optional] 
**localized_text** | **int** |  | [optional] 
**additional_info** | **str** |  | [optional] 
**inner_status_code** | **int** |  | [optional] 
**inner_diagnostic_info** | [**DiagnosticInfo**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.diagnostic_info import DiagnosticInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticInfo from a JSON string
diagnostic_info_instance = DiagnosticInfo.from_json(json)
# print the JSON string representation of the object
print(DiagnosticInfo.to_json())

# convert the object into a dict
diagnostic_info_dict = diagnostic_info_instance.to_dict()
# create an instance of DiagnosticInfo from a dict
diagnostic_info_from_dict = DiagnosticInfo.from_dict(diagnostic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


