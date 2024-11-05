# CreateMonitoredItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**timestamps_to_return** | **int** |  | [optional] 
**items_to_create** | [**List[MonitoredItemCreateRequest]**](MonitoredItemCreateRequest.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.create_monitored_items_request import CreateMonitoredItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMonitoredItemsRequest from a JSON string
create_monitored_items_request_instance = CreateMonitoredItemsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMonitoredItemsRequest.to_json())

# convert the object into a dict
create_monitored_items_request_dict = create_monitored_items_request_instance.to_dict()
# create an instance of CreateMonitoredItemsRequest from a dict
create_monitored_items_request_from_dict = CreateMonitoredItemsRequest.from_dict(create_monitored_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


