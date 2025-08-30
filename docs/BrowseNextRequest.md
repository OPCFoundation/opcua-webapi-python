# BrowseNextRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.3/#5.9.3.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**release_continuation_points** | **bool** |  | [optional] [default to False]
**continuation_points** | **List[bytearray]** |  | [optional] 

## Example

```python
from opcua_webapi.models.browse_next_request import BrowseNextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseNextRequest from a JSON string
browse_next_request_instance = BrowseNextRequest.from_json(json)
# print the JSON string representation of the object
print(BrowseNextRequest.to_json())

# convert the object into a dict
browse_next_request_dict = browse_next_request_instance.to_dict()
# create an instance of BrowseNextRequest from a dict
browse_next_request_from_dict = BrowseNextRequest.from_dict(browse_next_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


