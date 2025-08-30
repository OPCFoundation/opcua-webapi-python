# DeleteSubscriptionsResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.8/#5.14.8.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[StatusCode]**](StatusCode.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.delete_subscriptions_response import DeleteSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubscriptionsResponse from a JSON string
delete_subscriptions_response_instance = DeleteSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSubscriptionsResponse.to_json())

# convert the object into a dict
delete_subscriptions_response_dict = delete_subscriptions_response_instance.to_dict()
# create an instance of DeleteSubscriptionsResponse from a dict
delete_subscriptions_response_from_dict = DeleteSubscriptionsResponse.from_dict(delete_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


