# UpsertTemporalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | [**EntityCommonType**](EntityCommonType.md) |  | 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.upsert_temporal_request import UpsertTemporalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertTemporalRequest from a JSON string
upsert_temporal_request_instance = UpsertTemporalRequest.from_json(json)
# print the JSON string representation of the object
print UpsertTemporalRequest.to_json()

# convert the object into a dict
upsert_temporal_request_dict = upsert_temporal_request_instance.to_dict()
# create an instance of UpsertTemporalRequest from a dict
upsert_temporal_request_form_dict = upsert_temporal_request.from_dict(upsert_temporal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


