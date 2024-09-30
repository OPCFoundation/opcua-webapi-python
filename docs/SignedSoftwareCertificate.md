# SignedSoftwareCertificate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_data** | **bytearray** |  | [optional] 
**signature** | **bytearray** |  | [optional] 

## Example

```python
from opcua_webapi.models.signed_software_certificate import SignedSoftwareCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SignedSoftwareCertificate from a JSON string
signed_software_certificate_instance = SignedSoftwareCertificate.from_json(json)
# print the JSON string representation of the object
print SignedSoftwareCertificate.to_json()

# convert the object into a dict
signed_software_certificate_dict = signed_software_certificate_instance.to_dict()
# create an instance of SignedSoftwareCertificate from a dict
signed_software_certificate_form_dict = signed_software_certificate.from_dict(signed_software_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


