# Range

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part8/5.6.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low** | **float** |  | [optional] [default to 0]
**high** | **float** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print(Range.to_json())

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_from_dict = Range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


