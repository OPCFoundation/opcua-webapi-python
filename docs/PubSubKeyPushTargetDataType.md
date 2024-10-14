# PubSubKeyPushTargetDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uri** | **str** |  | [optional] 
**push_target_folder** | **List[str]** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**security_policy_uri** | **str** |  | [optional] 
**user_token_type** | [**UserTokenPolicy**](UserTokenPolicy.md) |  | [optional] 
**requested_key_count** | **int** |  | [optional] 
**retry_interval** | **float** |  | [optional] 
**push_target_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 
**security_groups** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.pub_sub_key_push_target_data_type import PubSubKeyPushTargetDataType

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubKeyPushTargetDataType from a JSON string
pub_sub_key_push_target_data_type_instance = PubSubKeyPushTargetDataType.from_json(json)
# print the JSON string representation of the object
print(PubSubKeyPushTargetDataType.to_json())

# convert the object into a dict
pub_sub_key_push_target_data_type_dict = pub_sub_key_push_target_data_type_instance.to_dict()
# create an instance of PubSubKeyPushTargetDataType from a dict
pub_sub_key_push_target_data_type_from_dict = PubSubKeyPushTargetDataType.from_dict(pub_sub_key_push_target_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


