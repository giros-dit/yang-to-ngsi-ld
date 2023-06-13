# Feature

5.2.29 This data type represents a spatially bounded Entity in GeoJSON format, as mandated by IETF RFC 7946. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | GeoJSON Type.  | 
**geometry** | [**Geometry**](Geometry.md) |  | 
**properties** | [**FeatureProperties**](FeatureProperties.md) |  | 
**context** | [**LdContext**](LdContext.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print Feature.to_json()

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_form_dict = feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


