# SystemProtectionPoliciesPolicy

 YANG module: srl_nokia-protection-policies.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SystemProtectionPoliciesPolicy. | [default to 'SystemProtectionPoliciesPolicy']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**protection_policy_name** | [**ProtectionPolicyName**](ProtectionPolicyName.md) |  | [optional] 
**revert_timer** | [**RevertTimer**](RevertTimer.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.system_protection_policies_policy import SystemProtectionPoliciesPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SystemProtectionPoliciesPolicy from a JSON string
system_protection_policies_policy_instance = SystemProtectionPoliciesPolicy.from_json(json)
# print the JSON string representation of the object
print(SystemProtectionPoliciesPolicy.to_json())

# convert the object into a dict
system_protection_policies_policy_dict = system_protection_policies_policy_instance.to_dict()
# create an instance of SystemProtectionPoliciesPolicy from a dict
system_protection_policies_policy_from_dict = SystemProtectionPoliciesPolicy.from_dict(system_protection_policies_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


