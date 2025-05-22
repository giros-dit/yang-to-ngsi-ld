# YANGIdentity

A representation schema for YANG Identities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be YANGIdentity. | [default to 'YANGIdentity']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**description** | [**YANGIdentityDescription**](YANGIdentityDescription.md) |  | 
**identifier** | [**YANGIdentityIdentifier**](YANGIdentityIdentifier.md) |  | 
**namespace** | [**YANGIdentityNamespace**](YANGIdentityNamespace.md) |  | 
**broader** | [**YANGIdentityBroader**](YANGIdentityBroader.md) |  | [optional] 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.yang_identity import YANGIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of YANGIdentity from a JSON string
yang_identity_instance = YANGIdentity.from_json(json)
# print the JSON string representation of the object
print(YANGIdentity.to_json())

# convert the object into a dict
yang_identity_dict = yang_identity_instance.to_dict()
# create an instance of YANGIdentity from a dict
yang_identity_from_dict = YANGIdentity.from_dict(yang_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


