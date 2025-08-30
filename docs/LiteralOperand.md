# LiteralOperand

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.7.4/#7.7.4.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Variant**](Variant.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.literal_operand import LiteralOperand

# TODO update the JSON string below
json = "{}"
# create an instance of LiteralOperand from a JSON string
literal_operand_instance = LiteralOperand.from_json(json)
# print the JSON string representation of the object
print(LiteralOperand.to_json())

# convert the object into a dict
literal_operand_dict = literal_operand_instance.to_dict()
# create an instance of LiteralOperand from a dict
literal_operand_from_dict = LiteralOperand.from_dict(literal_operand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


