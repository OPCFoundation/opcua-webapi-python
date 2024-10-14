# ContentFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[ContentFilterElement]**](ContentFilterElement.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.content_filter import ContentFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFilter from a JSON string
content_filter_instance = ContentFilter.from_json(json)
# print the JSON string representation of the object
print(ContentFilter.to_json())

# convert the object into a dict
content_filter_dict = content_filter_instance.to_dict()
# create an instance of ContentFilter from a dict
content_filter_from_dict = ContentFilter.from_dict(content_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


