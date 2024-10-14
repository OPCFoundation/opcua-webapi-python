# BrowseNextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[BrowseResult]**](BrowseResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_next_response import BrowseNextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseNextResponse from a JSON string
browse_next_response_instance = BrowseNextResponse.from_json(json)
# print the JSON string representation of the object
print(BrowseNextResponse.to_json())

# convert the object into a dict
browse_next_response_dict = browse_next_response_instance.to_dict()
# create an instance of BrowseNextResponse from a dict
browse_next_response_from_dict = BrowseNextResponse.from_dict(browse_next_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


