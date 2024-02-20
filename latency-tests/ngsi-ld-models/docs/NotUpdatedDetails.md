# NotUpdatedDetails

5.2.19 represents additional information provided by an implementation when an Attribute update did not happen. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Attribute name.  | 
**reason** | **str** | Reason for not having changed such Attribute.  | 
**registration_id** | **str** | Registration Id corresponding to a failed distributed operation (optional).  | [optional] 

## Example

```python
from ngsi_ld_models.models.not_updated_details import NotUpdatedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NotUpdatedDetails from a JSON string
not_updated_details_instance = NotUpdatedDetails.from_json(json)
# print the JSON string representation of the object
print NotUpdatedDetails.to_json()

# convert the object into a dict
not_updated_details_dict = not_updated_details_instance.to_dict()
# create an instance of NotUpdatedDetails from a dict
not_updated_details_form_dict = not_updated_details.from_dict(not_updated_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


