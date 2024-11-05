# TransferResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 
**available_sequence_numbers** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.transfer_result import TransferResult

# TODO update the JSON string below
json = "{}"
# create an instance of TransferResult from a JSON string
transfer_result_instance = TransferResult.from_json(json)
# print the JSON string representation of the object
print(TransferResult.to_json())

# convert the object into a dict
transfer_result_dict = transfer_result_instance.to_dict()
# create an instance of TransferResult from a dict
transfer_result_from_dict = TransferResult.from_dict(transfer_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


