# PublishResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**available_sequence_numbers** | **List[int]** |  | [optional] 
**more_notifications** | **bool** |  | [optional] [default to False]
**notification_message** | [**NotificationMessage**](NotificationMessage.md) |  | [optional] 
**results** | [**List[StatusCode]**](StatusCode.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.publish_response import PublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublishResponse from a JSON string
publish_response_instance = PublishResponse.from_json(json)
# print the JSON string representation of the object
print(PublishResponse.to_json())

# convert the object into a dict
publish_response_dict = publish_response_instance.to_dict()
# create an instance of PublishResponse from a dict
publish_response_from_dict = PublishResponse.from_dict(publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


