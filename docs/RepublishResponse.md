# RepublishResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**notification_message** | [**NotificationMessage**](NotificationMessage.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.republish_response import RepublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepublishResponse from a JSON string
republish_response_instance = RepublishResponse.from_json(json)
# print the JSON string representation of the object
print RepublishResponse.to_json()

# convert the object into a dict
republish_response_dict = republish_response_instance.to_dict()
# create an instance of RepublishResponse from a dict
republish_response_form_dict = republish_response.from_dict(republish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


