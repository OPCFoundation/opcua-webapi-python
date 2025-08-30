# BrowseResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.2/#5.9.2.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[BrowseResult]**](BrowseResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_response import BrowseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseResponse from a JSON string
browse_response_instance = BrowseResponse.from_json(json)
# print the JSON string representation of the object
print(BrowseResponse.to_json())

# convert the object into a dict
browse_response_dict = browse_response_instance.to_dict()
# create an instance of BrowseResponse from a dict
browse_response_from_dict = BrowseResponse.from_dict(browse_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


