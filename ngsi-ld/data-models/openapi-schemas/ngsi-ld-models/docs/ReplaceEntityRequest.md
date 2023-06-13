# ReplaceEntityRequest


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
from ngsi_ld_models.models.replace_entity_request import ReplaceEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceEntityRequest from a JSON string
replace_entity_request_instance = ReplaceEntityRequest.from_json(json)
# print the JSON string representation of the object
print ReplaceEntityRequest.to_json()

# convert the object into a dict
replace_entity_request_dict = replace_entity_request_instance.to_dict()
# create an instance of ReplaceEntityRequest from a dict
replace_entity_request_form_dict = replace_entity_request.from_dict(replace_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


