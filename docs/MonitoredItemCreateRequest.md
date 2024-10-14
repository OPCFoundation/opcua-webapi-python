# MonitoredItemCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_to_monitor** | [**ReadValueId**](ReadValueId.md) |  | [optional] 
**monitoring_mode** | **int** |  | [optional] 
**requested_parameters** | [**MonitoringParameters**](MonitoringParameters.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.monitored_item_create_request import MonitoredItemCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredItemCreateRequest from a JSON string
monitored_item_create_request_instance = MonitoredItemCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MonitoredItemCreateRequest.to_json())

# convert the object into a dict
monitored_item_create_request_dict = monitored_item_create_request_instance.to_dict()
# create an instance of MonitoredItemCreateRequest from a dict
monitored_item_create_request_from_dict = MonitoredItemCreateRequest.from_dict(monitored_item_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


