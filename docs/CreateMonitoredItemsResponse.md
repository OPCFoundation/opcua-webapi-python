# CreateMonitoredItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[MonitoredItemCreateResult]**](MonitoredItemCreateResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.create_monitored_items_response import CreateMonitoredItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMonitoredItemsResponse from a JSON string
create_monitored_items_response_instance = CreateMonitoredItemsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMonitoredItemsResponse.to_json())

# convert the object into a dict
create_monitored_items_response_dict = create_monitored_items_response_instance.to_dict()
# create an instance of CreateMonitoredItemsResponse from a dict
create_monitored_items_response_from_dict = CreateMonitoredItemsResponse.from_dict(create_monitored_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


