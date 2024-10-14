# ModifySubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**requested_publishing_interval** | **float** |  | [optional] 
**requested_lifetime_count** | **int** |  | [optional] 
**requested_max_keep_alive_count** | **int** |  | [optional] 
**max_notifications_per_publish** | **int** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.modify_subscription_request import ModifySubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySubscriptionRequest from a JSON string
modify_subscription_request_instance = ModifySubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(ModifySubscriptionRequest.to_json())

# convert the object into a dict
modify_subscription_request_dict = modify_subscription_request_instance.to_dict()
# create an instance of ModifySubscriptionRequest from a dict
modify_subscription_request_from_dict = ModifySubscriptionRequest.from_dict(modify_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


