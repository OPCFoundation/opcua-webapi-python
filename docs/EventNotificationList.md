# EventNotificationList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventFieldList]**](EventFieldList.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.event_notification_list import EventNotificationList

# TODO update the JSON string below
json = "{}"
# create an instance of EventNotificationList from a JSON string
event_notification_list_instance = EventNotificationList.from_json(json)
# print the JSON string representation of the object
print EventNotificationList.to_json()

# convert the object into a dict
event_notification_list_dict = event_notification_list_instance.to_dict()
# create an instance of EventNotificationList from a dict
event_notification_list_form_dict = event_notification_list.from_dict(event_notification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


