# SetPublishingModeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[StatusCode]**](StatusCode.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.set_publishing_mode_response import SetPublishingModeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetPublishingModeResponse from a JSON string
set_publishing_mode_response_instance = SetPublishingModeResponse.from_json(json)
# print the JSON string representation of the object
print(SetPublishingModeResponse.to_json())

# convert the object into a dict
set_publishing_mode_response_dict = set_publishing_mode_response_instance.to_dict()
# create an instance of SetPublishingModeResponse from a dict
set_publishing_mode_response_from_dict = SetPublishingModeResponse.from_dict(set_publishing_mode_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


