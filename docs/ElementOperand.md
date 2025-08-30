# ElementOperand

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.7.4/#7.7.4.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.element_operand import ElementOperand

# TODO update the JSON string below
json = "{}"
# create an instance of ElementOperand from a JSON string
element_operand_instance = ElementOperand.from_json(json)
# print the JSON string representation of the object
print(ElementOperand.to_json())

# convert the object into a dict
element_operand_dict = element_operand_instance.to_dict()
# create an instance of ElementOperand from a dict
element_operand_from_dict = ElementOperand.from_dict(element_operand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


