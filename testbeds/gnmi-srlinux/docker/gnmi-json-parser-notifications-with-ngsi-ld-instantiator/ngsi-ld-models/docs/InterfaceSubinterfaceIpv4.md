# InterfaceSubinterfaceIpv4

IPv4 configuration and state for the subinterface  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfaceIpv4. | [default to 'InterfaceSubinterfaceIpv4']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**admin_state** | [**InterfaceSubinterfaceIpv4AdminState**](InterfaceSubinterfaceIpv4AdminState.md) |  | [optional] 
**allow_directed_broadcast** | [**AllowDirectedBroadcast**](AllowDirectedBroadcast.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterface_ipv4 import InterfaceSubinterfaceIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv4 from a JSON string
interface_subinterface_ipv4_instance = InterfaceSubinterfaceIpv4.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv4.to_json()

# convert the object into a dict
interface_subinterface_ipv4_dict = interface_subinterface_ipv4_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv4 from a dict
interface_subinterface_ipv4_form_dict = interface_subinterface_ipv4.from_dict(interface_subinterface_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


