# ContextSourceIdentity

5.2.40 This type represents the data uniquely identifying a Context Source,  and if the Context Source supports multi-tenancy (see clause 4.14) uniquely  identifying a Tenant within that Context Source. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Context Source ID.  | 
**type** | **str** | Node type.  | [default to 'ContextSourceIdentity']
**context_source_extras** | **object** | Instance specific information relevant to the configuration  of the Context Source itself in raw unexpandable JSON which  shall not be interpreted as JSON-LD using the supplied @context.  | [optional] 
**context_source_up_time** | **str** | Total Duration that the Context Source has been available.  | 
**context_source_time_at** | **datetime** | Current time observed at the Context Source. Timestamp. See clause 4.8.  | 
**context_source_alias** | **str** | A unique id for a Context Source which can be used to identify loops.  In the multi-tenancy use case (see clause 4.14), this id shall be  used to identify a specific Tenant within a registered Context Source.  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.context_source_identity import ContextSourceIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ContextSourceIdentity from a JSON string
context_source_identity_instance = ContextSourceIdentity.from_json(json)
# print the JSON string representation of the object
print(ContextSourceIdentity.to_json())

# convert the object into a dict
context_source_identity_dict = context_source_identity_instance.to_dict()
# create an instance of ContextSourceIdentity from a dict
context_source_identity_from_dict = ContextSourceIdentity.from_dict(context_source_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


