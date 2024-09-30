# TransferSubscriptionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[TransferResult]**](TransferResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.transfer_subscriptions_response import TransferSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferSubscriptionsResponse from a JSON string
transfer_subscriptions_response_instance = TransferSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print TransferSubscriptionsResponse.to_json()

# convert the object into a dict
transfer_subscriptions_response_dict = transfer_subscriptions_response_instance.to_dict()
# create an instance of TransferSubscriptionsResponse from a dict
transfer_subscriptions_response_form_dict = transfer_subscriptions_response.from_dict(transfer_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


