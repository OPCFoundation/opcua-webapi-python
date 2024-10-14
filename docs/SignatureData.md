# SignatureData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | [optional] 
**signature** | **bytearray** |  | [optional] 

## Example

```python
from opcua_webapi.models.signature_data import SignatureData

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureData from a JSON string
signature_data_instance = SignatureData.from_json(json)
# print the JSON string representation of the object
print(SignatureData.to_json())

# convert the object into a dict
signature_data_dict = signature_data_instance.to_dict()
# create an instance of SignatureData from a dict
signature_data_from_dict = SignatureData.from_dict(signature_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


