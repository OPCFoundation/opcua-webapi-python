# SetTriggeringResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**add_results** | **List[int]** |  | [optional] 
**add_diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 
**remove_results** | **List[int]** |  | [optional] 
**remove_diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.set_triggering_response import SetTriggeringResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetTriggeringResponse from a JSON string
set_triggering_response_instance = SetTriggeringResponse.from_json(json)
# print the JSON string representation of the object
print SetTriggeringResponse.to_json()

# convert the object into a dict
set_triggering_response_dict = set_triggering_response_instance.to_dict()
# create an instance of SetTriggeringResponse from a dict
set_triggering_response_form_dict = set_triggering_response.from_dict(set_triggering_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


