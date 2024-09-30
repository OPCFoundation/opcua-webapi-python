# Decimal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.decimal import Decimal

# TODO update the JSON string below
json = "{}"
# create an instance of Decimal from a JSON string
decimal_instance = Decimal.from_json(json)
# print the JSON string representation of the object
print Decimal.to_json()

# convert the object into a dict
decimal_dict = decimal_instance.to_dict()
# create an instance of Decimal from a dict
decimal_form_dict = decimal.from_dict(decimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


