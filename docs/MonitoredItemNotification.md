# MonitoredItemNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_handle** | **int** |  | [optional] 
**value** | [**DataValue**](DataValue.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.monitored_item_notification import MonitoredItemNotification

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredItemNotification from a JSON string
monitored_item_notification_instance = MonitoredItemNotification.from_json(json)
# print the JSON string representation of the object
print(MonitoredItemNotification.to_json())

# convert the object into a dict
monitored_item_notification_dict = monitored_item_notification_instance.to_dict()
# create an instance of MonitoredItemNotification from a dict
monitored_item_notification_from_dict = MonitoredItemNotification.from_dict(monitored_item_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


