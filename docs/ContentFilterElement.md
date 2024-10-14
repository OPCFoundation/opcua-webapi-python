# ContentFilterElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_operator** | **int** |  | [optional] 
**filter_operands** | [**List[ExtensionObject]**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.content_filter_element import ContentFilterElement

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFilterElement from a JSON string
content_filter_element_instance = ContentFilterElement.from_json(json)
# print the JSON string representation of the object
print(ContentFilterElement.to_json())

# convert the object into a dict
content_filter_element_dict = content_filter_element_instance.to_dict()
# create an instance of ContentFilterElement from a dict
content_filter_element_from_dict = ContentFilterElement.from_dict(content_filter_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


