# AppendAttrsTemporalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.append_attrs_temporal_request import AppendAttrsTemporalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppendAttrsTemporalRequest from a JSON string
append_attrs_temporal_request_instance = AppendAttrsTemporalRequest.from_json(json)
# print the JSON string representation of the object
print AppendAttrsTemporalRequest.to_json()

# convert the object into a dict
append_attrs_temporal_request_dict = append_attrs_temporal_request_instance.to_dict()
# create an instance of AppendAttrsTemporalRequest from a dict
append_attrs_temporal_request_form_dict = append_attrs_temporal_request.from_dict(append_attrs_temporal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


