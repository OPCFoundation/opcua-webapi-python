# StatusChangeNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**diagnostic_info** | [**DiagnosticInfo**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.status_change_notification import StatusChangeNotification

# TODO update the JSON string below
json = "{}"
# create an instance of StatusChangeNotification from a JSON string
status_change_notification_instance = StatusChangeNotification.from_json(json)
# print the JSON string representation of the object
print(StatusChangeNotification.to_json())

# convert the object into a dict
status_change_notification_dict = status_change_notification_instance.to_dict()
# create an instance of StatusChangeNotification from a dict
status_change_notification_from_dict = StatusChangeNotification.from_dict(status_change_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


