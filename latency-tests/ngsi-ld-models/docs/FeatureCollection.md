# FeatureCollection

5.2.30 This data type represents a list of spatially bounded Entities in GeoJSON format, as mandated by IETF RFC 7946. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Type.  | 
**features** | [**List[Feature]**](Feature.md) | In the case that no matches are found, \&quot;features\&quot; will be an empty array.  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.feature_collection import FeatureCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureCollection from a JSON string
feature_collection_instance = FeatureCollection.from_json(json)
# print the JSON string representation of the object
print FeatureCollection.to_json()

# convert the object into a dict
feature_collection_dict = feature_collection_instance.to_dict()
# create an instance of FeatureCollection from a dict
feature_collection_form_dict = feature_collection.from_dict(feature_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


