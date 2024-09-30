# GetEndpointsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**locale_ids** | **List[str]** |  | [optional] 
**profile_uris** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.get_endpoints_request import GetEndpointsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointsRequest from a JSON string
get_endpoints_request_instance = GetEndpointsRequest.from_json(json)
# print the JSON string representation of the object
print GetEndpointsRequest.to_json()

# convert the object into a dict
get_endpoints_request_dict = get_endpoints_request_instance.to_dict()
# create an instance of GetEndpointsRequest from a dict
get_endpoints_request_form_dict = get_endpoints_request.from_dict(get_endpoints_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


