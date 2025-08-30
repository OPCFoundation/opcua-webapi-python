# ApplicationDescription

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.3.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uri** | **str** |  | [optional] 
**product_uri** | **str** |  | [optional] 
**application_name** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**application_type** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.4). | [optional] 
**gateway_server_uri** | **str** |  | [optional] 
**discovery_profile_uri** | **str** |  | [optional] 
**discovery_urls** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.application_description import ApplicationDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDescription from a JSON string
application_description_instance = ApplicationDescription.from_json(json)
# print the JSON string representation of the object
print(ApplicationDescription.to_json())

# convert the object into a dict
application_description_dict = application_description_instance.to_dict()
# create an instance of ApplicationDescription from a dict
application_description_from_dict = ApplicationDescription.from_dict(application_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


