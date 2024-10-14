# AttributeOperand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**browse_path** | [**RelativePath**](RelativePath.md) |  | [optional] 
**attribute_id** | **int** |  | [optional] 
**index_range** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.attribute_operand import AttributeOperand

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeOperand from a JSON string
attribute_operand_instance = AttributeOperand.from_json(json)
# print the JSON string representation of the object
print(AttributeOperand.to_json())

# convert the object into a dict
attribute_operand_dict = attribute_operand_instance.to_dict()
# create an instance of AttributeOperand from a dict
attribute_operand_from_dict = AttributeOperand.from_dict(attribute_operand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


