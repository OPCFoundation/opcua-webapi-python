# CancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**cancel_count** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.cancel_response import CancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelResponse from a JSON string
cancel_response_instance = CancelResponse.from_json(json)
# print the JSON string representation of the object
print(CancelResponse.to_json())

# convert the object into a dict
cancel_response_dict = cancel_response_instance.to_dict()
# create an instance of CancelResponse from a dict
cancel_response_from_dict = CancelResponse.from_dict(cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


