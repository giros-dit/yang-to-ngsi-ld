# InterfaceEthernetExponentialPortDampening

Exponential port dampening parameters  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceEthernetExponentialPortDampening. | [default to 'InterfaceEthernetExponentialPortDampening']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**admin_state** | [**InterfaceEthernetExponentialPortDampeningAdminState**](InterfaceEthernetExponentialPortDampeningAdminState.md) |  | [optional] 
**half_life** | [**HalfLife**](HalfLife.md) |  | [optional] 
**max_suppress_time** | [**MaxSuppressTime**](MaxSuppressTime.md) |  | [optional] 
**reuse_threshold** | [**ReuseThreshold**](ReuseThreshold.md) |  | [optional] 
**suppress_threshold** | [**SuppressThreshold**](SuppressThreshold.md) |  | [optional] 
**current_penalties** | [**CurrentPenalties**](CurrentPenalties.md) |  | [optional] 
**max_penalties** | [**MaxPenalties**](MaxPenalties.md) |  | [optional] 
**oper_state** | [**InterfaceEthernetExponentialPortDampeningOperState**](InterfaceEthernetExponentialPortDampeningOperState.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ethernet_exponential_port_dampening import InterfaceEthernetExponentialPortDampening

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceEthernetExponentialPortDampening from a JSON string
interface_ethernet_exponential_port_dampening_instance = InterfaceEthernetExponentialPortDampening.from_json(json)
# print the JSON string representation of the object
print(InterfaceEthernetExponentialPortDampening.to_json())

# convert the object into a dict
interface_ethernet_exponential_port_dampening_dict = interface_ethernet_exponential_port_dampening_instance.to_dict()
# create an instance of InterfaceEthernetExponentialPortDampening from a dict
interface_ethernet_exponential_port_dampening_from_dict = InterfaceEthernetExponentialPortDampening.from_dict(interface_ethernet_exponential_port_dampening_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


