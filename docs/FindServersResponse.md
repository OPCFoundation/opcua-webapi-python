# FindServersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**servers** | [**List[ApplicationDescription]**](ApplicationDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.find_servers_response import FindServersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindServersResponse from a JSON string
find_servers_response_instance = FindServersResponse.from_json(json)
# print the JSON string representation of the object
print(FindServersResponse.to_json())

# convert the object into a dict
find_servers_response_dict = find_servers_response_instance.to_dict()
# create an instance of FindServersResponse from a dict
find_servers_response_from_dict = FindServersResponse.from_dict(find_servers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


