# CreateSessionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**session_id** | **str** |  | [optional] 
**authentication_token** | **str** |  | [optional] 
**revised_session_timeout** | **float** |  | [optional] 
**server_nonce** | **bytearray** |  | [optional] 
**server_certificate** | **bytearray** |  | [optional] 
**server_endpoints** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 
**server_software_certificates** | [**List[SignedSoftwareCertificate]**](SignedSoftwareCertificate.md) |  | [optional] 
**server_signature** | [**SignatureData**](SignatureData.md) |  | [optional] 
**max_request_message_size** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.create_session_response import CreateSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionResponse from a JSON string
create_session_response_instance = CreateSessionResponse.from_json(json)
# print the JSON string representation of the object
print CreateSessionResponse.to_json()

# convert the object into a dict
create_session_response_dict = create_session_response_instance.to_dict()
# create an instance of CreateSessionResponse from a dict
create_session_response_form_dict = create_session_response.from_dict(create_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


