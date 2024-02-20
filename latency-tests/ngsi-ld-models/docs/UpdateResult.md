# UpdateResult

5.2.18 represents the result of Attribute update (append or update) operations in the NGSI-LD API regardless of whether local or distributed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated** | **List[str]** | List of Attributes (represented by their Name) that were appended or updated.  | 
**not_updated** | [**List[NotUpdatedDetails]**](NotUpdatedDetails.md) | List which contains the Attributes (represented by their Name) that were not updated, together with the reason for not being updated.  | 

## Example

```python
from ngsi_ld_models.models.update_result import UpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResult from a JSON string
update_result_instance = UpdateResult.from_json(json)
# print the JSON string representation of the object
print UpdateResult.to_json()

# convert the object into a dict
update_result_dict = update_result_instance.to_dict()
# create an instance of UpdateResult from a dict
update_result_form_dict = update_result.from_dict(update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


