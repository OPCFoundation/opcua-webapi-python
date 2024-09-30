# CreateSessionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**client_description** | [**ApplicationDescription**](ApplicationDescription.md) |  | [optional] 
**server_uri** | **str** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**session_name** | **str** |  | [optional] 
**client_nonce** | **bytearray** |  | [optional] 
**client_certificate** | **bytearray** |  | [optional] 
**requested_session_timeout** | **float** |  | [optional] 
**max_response_message_size** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.create_session_request import CreateSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionRequest from a JSON string
create_session_request_instance = CreateSessionRequest.from_json(json)
# print the JSON string representation of the object
print CreateSessionRequest.to_json()

# convert the object into a dict
create_session_request_dict = create_session_request_instance.to_dict()
# create an instance of CreateSessionRequest from a dict
create_session_request_form_dict = create_session_request.from_dict(create_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


