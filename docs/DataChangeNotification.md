# DataChangeNotification

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.25.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitored_items** | [**List[MonitoredItemNotification]**](MonitoredItemNotification.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.data_change_notification import DataChangeNotification

# TODO update the JSON string below
json = "{}"
# create an instance of DataChangeNotification from a JSON string
data_change_notification_instance = DataChangeNotification.from_json(json)
# print the JSON string representation of the object
print(DataChangeNotification.to_json())

# convert the object into a dict
data_change_notification_dict = data_change_notification_instance.to_dict()
# create an instance of DataChangeNotification from a dict
data_change_notification_from_dict = DataChangeNotification.from_dict(data_change_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


