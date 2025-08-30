# ModifyMonitoredItemsRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.3/#5.13.3.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**timestamps_to_return** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.39). | [optional] 
**items_to_modify** | [**List[MonitoredItemModifyRequest]**](MonitoredItemModifyRequest.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.modify_monitored_items_request import ModifyMonitoredItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyMonitoredItemsRequest from a JSON string
modify_monitored_items_request_instance = ModifyMonitoredItemsRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyMonitoredItemsRequest.to_json())

# convert the object into a dict
modify_monitored_items_request_dict = modify_monitored_items_request_instance.to_dict()
# create an instance of ModifyMonitoredItemsRequest from a dict
modify_monitored_items_request_from_dict = ModifyMonitoredItemsRequest.from_dict(modify_monitored_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


