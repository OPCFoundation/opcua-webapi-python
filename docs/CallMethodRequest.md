# CallMethodRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.12.2/#5.12.2.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** |  | [optional] 
**method_id** | **str** |  | [optional] 
**input_arguments** | [**List[Variant]**](Variant.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.call_method_request import CallMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallMethodRequest from a JSON string
call_method_request_instance = CallMethodRequest.from_json(json)
# print the JSON string representation of the object
print(CallMethodRequest.to_json())

# convert the object into a dict
call_method_request_dict = call_method_request_instance.to_dict()
# create an instance of CallMethodRequest from a dict
call_method_request_from_dict = CallMethodRequest.from_dict(call_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


