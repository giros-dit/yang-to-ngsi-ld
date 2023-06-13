# FeatureProperties

5.2.31 This data type represents the type and the associated attributes (Properties and Relationships) of an Entity in GeoJSON format. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FeaturePropertiesType**](FeaturePropertiesType.md) |  | 

## Example

```python
from ngsi_ld_models.models.feature_properties import FeatureProperties

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureProperties from a JSON string
feature_properties_instance = FeatureProperties.from_json(json)
# print the JSON string representation of the object
print FeatureProperties.to_json()

# convert the object into a dict
feature_properties_dict = feature_properties_instance.to_dict()
# create an instance of FeatureProperties from a dict
feature_properties_form_dict = feature_properties.from_dict(feature_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


