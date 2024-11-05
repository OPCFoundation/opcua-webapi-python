# CloseSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**delete_subscriptions** | **bool** |  | [optional] [default to False]

## Example

```python
from opcua_webapi.models.close_session_request import CloseSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseSessionRequest from a JSON string
close_session_request_instance = CloseSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CloseSessionRequest.to_json())

# convert the object into a dict
close_session_request_dict = close_session_request_instance.to_dict()
# create an instance of CloseSessionRequest from a dict
close_session_request_from_dict = CloseSessionRequest.from_dict(close_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


