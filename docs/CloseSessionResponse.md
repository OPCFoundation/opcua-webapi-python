# CloseSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.close_session_response import CloseSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloseSessionResponse from a JSON string
close_session_response_instance = CloseSessionResponse.from_json(json)
# print the JSON string representation of the object
print(CloseSessionResponse.to_json())

# convert the object into a dict
close_session_response_dict = close_session_response_instance.to_dict()
# create an instance of CloseSessionResponse from a dict
close_session_response_from_dict = CloseSessionResponse.from_dict(close_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


