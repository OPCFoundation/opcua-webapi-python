# DeleteMonitoredItemsRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.6/#5.13.6.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**monitored_item_ids** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.delete_monitored_items_request import DeleteMonitoredItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMonitoredItemsRequest from a JSON string
delete_monitored_items_request_instance = DeleteMonitoredItemsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMonitoredItemsRequest.to_json())

# convert the object into a dict
delete_monitored_items_request_dict = delete_monitored_items_request_instance.to_dict()
# create an instance of DeleteMonitoredItemsRequest from a dict
delete_monitored_items_request_from_dict = DeleteMonitoredItemsRequest.from_dict(delete_monitored_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


