# ReadAnnotationDataDetails

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part11/6.5.6/#6.5.6.1).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**req_times** | **List[datetime]** |  | [optional] 

## Example

```python
from opcua_webapi.models.read_annotation_data_details import ReadAnnotationDataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAnnotationDataDetails from a JSON string
read_annotation_data_details_instance = ReadAnnotationDataDetails.from_json(json)
# print the JSON string representation of the object
print(ReadAnnotationDataDetails.to_json())

# convert the object into a dict
read_annotation_data_details_dict = read_annotation_data_details_instance.to_dict()
# create an instance of ReadAnnotationDataDetails from a dict
read_annotation_data_details_from_dict = ReadAnnotationDataDetails.from_dict(read_annotation_data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


