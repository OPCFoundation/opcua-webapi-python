# BrowseResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**continuation_point** | **bytearray** |  | [optional] 
**references** | [**List[ReferenceDescription]**](ReferenceDescription.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_result import BrowseResult

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseResult from a JSON string
browse_result_instance = BrowseResult.from_json(json)
# print the JSON string representation of the object
print BrowseResult.to_json()

# convert the object into a dict
browse_result_dict = browse_result_instance.to_dict()
# create an instance of BrowseResult from a dict
browse_result_form_dict = browse_result.from_dict(browse_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


