# DeleteSubscriptionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_ids** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.delete_subscriptions_request import DeleteSubscriptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubscriptionsRequest from a JSON string
delete_subscriptions_request_instance = DeleteSubscriptionsRequest.from_json(json)
# print the JSON string representation of the object
print DeleteSubscriptionsRequest.to_json()

# convert the object into a dict
delete_subscriptions_request_dict = delete_subscriptions_request_instance.to_dict()
# create an instance of DeleteSubscriptionsRequest from a dict
delete_subscriptions_request_form_dict = delete_subscriptions_request.from_dict(delete_subscriptions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


