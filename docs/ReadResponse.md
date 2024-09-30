# ReadResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[DataValue]**](DataValue.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.read_response import ReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadResponse from a JSON string
read_response_instance = ReadResponse.from_json(json)
# print the JSON string representation of the object
print ReadResponse.to_json()

# convert the object into a dict
read_response_dict = read_response_instance.to_dict()
# create an instance of ReadResponse from a dict
read_response_form_dict = read_response.from_dict(read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


