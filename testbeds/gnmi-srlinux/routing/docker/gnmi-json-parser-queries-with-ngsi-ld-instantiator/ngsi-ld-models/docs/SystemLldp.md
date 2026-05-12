# SystemLldp

Top-level container for LLDP configuration and state data  YANG module: srl_nokia-lldp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SystemLldp. | [default to 'SystemLldp']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**trace_options** | [**SystemLldpTraceOptions**](SystemLldpTraceOptions.md) |  | [optional] 
**admin_state** | [**SystemLldpAdminState**](SystemLldpAdminState.md) |  | [optional] 
**hello_timer** | [**HelloTimer**](HelloTimer.md) |  | [optional] 
**hold_multiplier** | [**HoldMultiplier**](HoldMultiplier.md) |  | [optional] 
**system_name** | [**SystemLldpSystemName**](SystemLldpSystemName.md) |  | [optional] 
**system_description** | [**SystemLldpSystemDescription**](SystemLldpSystemDescription.md) |  | [optional] 
**chassis_id** | [**SystemLldpChassisId**](SystemLldpChassisId.md) |  | [optional] 
**chassis_id_type** | [**SystemLldpChassisIdType**](SystemLldpChassisIdType.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.system_lldp import SystemLldp

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLldp from a JSON string
system_lldp_instance = SystemLldp.from_json(json)
# print the JSON string representation of the object
print(SystemLldp.to_json())

# convert the object into a dict
system_lldp_dict = system_lldp_instance.to_dict()
# create an instance of SystemLldp from a dict
system_lldp_from_dict = SystemLldp.from_dict(system_lldp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


