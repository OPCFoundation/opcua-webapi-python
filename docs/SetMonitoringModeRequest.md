# SetMonitoringModeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**monitoring_mode** | **int** |  | [optional] 
**monitored_item_ids** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.set_monitoring_mode_request import SetMonitoringModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMonitoringModeRequest from a JSON string
set_monitoring_mode_request_instance = SetMonitoringModeRequest.from_json(json)
# print the JSON string representation of the object
print(SetMonitoringModeRequest.to_json())

# convert the object into a dict
set_monitoring_mode_request_dict = set_monitoring_mode_request_instance.to_dict()
# create an instance of SetMonitoringModeRequest from a dict
set_monitoring_mode_request_from_dict = SetMonitoringModeRequest.from_dict(set_monitoring_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


