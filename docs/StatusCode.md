# StatusCode

[Link to specification](https://reference.opcfoundation.org/Core/Part4/v105/docs/7.39). [Set of defined codes](https://github.com/OPCFoundation/UA-Nodeset/tree/latest/Schema/StatusCode.csv).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.status_code import StatusCode

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCode from a JSON string
status_code_instance = StatusCode.from_json(json)
# print the JSON string representation of the object
print(StatusCode.to_json())

# convert the object into a dict
status_code_dict = status_code_instance.to_dict()
# create an instance of StatusCode from a dict
status_code_from_dict = StatusCode.from_dict(status_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


