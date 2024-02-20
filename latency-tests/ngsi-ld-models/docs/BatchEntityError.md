# BatchEntityError

5.2.17 represents an error raised (associated to a particular Entity) during the execution of a batch or distributed operation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Entity Id corresponding to the Entity in error.  | 
**registration_id** | **str** | Registration Id corresponding to a failed distributed operation (optional).  | [optional] 
**error** | [**ProblemDetails**](ProblemDetails.md) |  | 

## Example

```python
from ngsi_ld_models.models.batch_entity_error import BatchEntityError

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEntityError from a JSON string
batch_entity_error_instance = BatchEntityError.from_json(json)
# print the JSON string representation of the object
print BatchEntityError.to_json()

# convert the object into a dict
batch_entity_error_dict = batch_entity_error_instance.to_dict()
# create an instance of BatchEntityError from a dict
batch_entity_error_form_dict = batch_entity_error.from_dict(batch_entity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


