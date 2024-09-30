# FindServersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**locale_ids** | **List[str]** |  | [optional] 
**server_uris** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.find_servers_request import FindServersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindServersRequest from a JSON string
find_servers_request_instance = FindServersRequest.from_json(json)
# print the JSON string representation of the object
print FindServersRequest.to_json()

# convert the object into a dict
find_servers_request_dict = find_servers_request_instance.to_dict()
# create an instance of FindServersRequest from a dict
find_servers_request_form_dict = find_servers_request.from_dict(find_servers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


