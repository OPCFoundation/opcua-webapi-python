# SetMonitoringModeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | **List[int]** |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.set_monitoring_mode_response import SetMonitoringModeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetMonitoringModeResponse from a JSON string
set_monitoring_mode_response_instance = SetMonitoringModeResponse.from_json(json)
# print the JSON string representation of the object
print SetMonitoringModeResponse.to_json()

# convert the object into a dict
set_monitoring_mode_response_dict = set_monitoring_mode_response_instance.to_dict()
# create an instance of SetMonitoringModeResponse from a dict
set_monitoring_mode_response_form_dict = set_monitoring_mode_response.from_dict(set_monitoring_mode_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


