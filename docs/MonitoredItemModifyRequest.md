# MonitoredItemModifyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitored_item_id** | **int** |  | [optional] 
**requested_parameters** | [**MonitoringParameters**](MonitoringParameters.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.monitored_item_modify_request import MonitoredItemModifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredItemModifyRequest from a JSON string
monitored_item_modify_request_instance = MonitoredItemModifyRequest.from_json(json)
# print the JSON string representation of the object
print MonitoredItemModifyRequest.to_json()

# convert the object into a dict
monitored_item_modify_request_dict = monitored_item_modify_request_instance.to_dict()
# create an instance of MonitoredItemModifyRequest from a dict
monitored_item_modify_request_form_dict = monitored_item_modify_request.from_dict(monitored_item_modify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


