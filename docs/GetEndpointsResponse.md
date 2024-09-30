# GetEndpointsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**endpoints** | [**List[EndpointDescription]**](EndpointDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.get_endpoints_response import GetEndpointsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointsResponse from a JSON string
get_endpoints_response_instance = GetEndpointsResponse.from_json(json)
# print the JSON string representation of the object
print GetEndpointsResponse.to_json()

# convert the object into a dict
get_endpoints_response_dict = get_endpoints_response_instance.to_dict()
# create an instance of GetEndpointsResponse from a dict
get_endpoints_response_form_dict = get_endpoints_response.from_dict(get_endpoints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


