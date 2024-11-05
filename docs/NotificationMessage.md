# NotificationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_number** | **int** |  | [optional] [default to 0]
**publish_time** | **datetime** |  | [optional] 
**notification_data** | [**List[ExtensionObject]**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.notification_message import NotificationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationMessage from a JSON string
notification_message_instance = NotificationMessage.from_json(json)
# print the JSON string representation of the object
print(NotificationMessage.to_json())

# convert the object into a dict
notification_message_dict = notification_message_instance.to_dict()
# create an instance of NotificationMessage from a dict
notification_message_from_dict = NotificationMessage.from_dict(notification_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


