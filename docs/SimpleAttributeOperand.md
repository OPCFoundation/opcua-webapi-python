# SimpleAttributeOperand

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.7.4/#7.7.4.5).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_definition_id** | **str** |  | [optional] 
**browse_path** | **List[str]** |  | [optional] 
**attribute_id** | **int** |  | [optional] [default to 0]
**index_range** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.simple_attribute_operand import SimpleAttributeOperand

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAttributeOperand from a JSON string
simple_attribute_operand_instance = SimpleAttributeOperand.from_json(json)
# print the JSON string representation of the object
print(SimpleAttributeOperand.to_json())

# convert the object into a dict
simple_attribute_operand_dict = simple_attribute_operand_instance.to_dict()
# create an instance of SimpleAttributeOperand from a dict
simple_attribute_operand_from_dict = SimpleAttributeOperand.from_dict(simple_attribute_operand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


