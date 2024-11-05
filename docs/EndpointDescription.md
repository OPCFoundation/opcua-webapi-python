# EndpointDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_url** | **str** |  | [optional] 
**server** | [**ApplicationDescription**](ApplicationDescription.md) |  | [optional] 
**server_certificate** | **bytearray** |  | [optional] 
**security_mode** | **int** |  | [optional] 
**security_policy_uri** | **str** |  | [optional] 
**user_identity_tokens** | [**List[UserTokenPolicy]**](UserTokenPolicy.md) |  | [optional] 
**transport_profile_uri** | **str** |  | [optional] 
**security_level** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.endpoint_description import EndpointDescription

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDescription from a JSON string
endpoint_description_instance = EndpointDescription.from_json(json)
# print the JSON string representation of the object
print(EndpointDescription.to_json())

# convert the object into a dict
endpoint_description_dict = endpoint_description_instance.to_dict()
# create an instance of EndpointDescription from a dict
endpoint_description_from_dict = EndpointDescription.from_dict(endpoint_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


