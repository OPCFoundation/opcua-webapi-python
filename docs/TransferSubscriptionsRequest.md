# TransferSubscriptionsRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.7/#5.14.7.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_ids** | **List[int]** |  | [optional] 
**send_initial_values** | **bool** |  | [optional] [default to False]

## Example

```python
from opcua_webapi.models.transfer_subscriptions_request import TransferSubscriptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferSubscriptionsRequest from a JSON string
transfer_subscriptions_request_instance = TransferSubscriptionsRequest.from_json(json)
# print the JSON string representation of the object
print(TransferSubscriptionsRequest.to_json())

# convert the object into a dict
transfer_subscriptions_request_dict = transfer_subscriptions_request_instance.to_dict()
# create an instance of TransferSubscriptionsRequest from a dict
transfer_subscriptions_request_from_dict = TransferSubscriptionsRequest.from_dict(transfer_subscriptions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


