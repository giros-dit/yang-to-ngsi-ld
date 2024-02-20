# FeaturePropertiesType

Entity Type (or JSON array, in case of Entities with multiple Entity Types). Both short hand string (type name) or URI are allowed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models.models.feature_properties_type import FeaturePropertiesType

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePropertiesType from a JSON string
feature_properties_type_instance = FeaturePropertiesType.from_json(json)
# print the JSON string representation of the object
print FeaturePropertiesType.to_json()

# convert the object into a dict
feature_properties_type_dict = feature_properties_type_instance.to_dict()
# create an instance of FeaturePropertiesType from a dict
feature_properties_type_form_dict = feature_properties_type.from_dict(feature_properties_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


