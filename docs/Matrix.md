# Matrix

[Link to specification](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.4.5).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array** | **List[object]** |  | [optional] 
**dimensions** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.matrix import Matrix

# TODO update the JSON string below
json = "{}"
# create an instance of Matrix from a JSON string
matrix_instance = Matrix.from_json(json)
# print the JSON string representation of the object
print(Matrix.to_json())

# convert the object into a dict
matrix_dict = matrix_instance.to_dict()
# create an instance of Matrix from a dict
matrix_from_dict = Matrix.from_dict(matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


