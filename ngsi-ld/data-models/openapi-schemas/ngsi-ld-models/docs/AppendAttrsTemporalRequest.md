# AppendAttrsTemporalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | Entity Type(s). Both short hand string(s) (type name) or URI(s) are allowed.  | [optional] 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
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


