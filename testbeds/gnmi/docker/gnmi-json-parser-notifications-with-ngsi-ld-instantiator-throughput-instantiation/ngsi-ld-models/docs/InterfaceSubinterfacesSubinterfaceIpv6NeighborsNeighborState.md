# InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState

State data for each IPv6 address on the interface  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState. | [default to 'InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ip** | [**InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateIp**](InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateIp.md) |  | [optional] 
**link_layer_address** | [**InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateLinkLayerAddress**](InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateLinkLayerAddress.md) |  | 
**origin** | [**InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateOrigin**](InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateOrigin.md) |  | [optional] 
**is_router** | [**InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateIsRouter**](InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateIsRouter.md) |  | [optional] 
**neighbor_state** | [**InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateNeighborState**](InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborStateNeighborState.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state import InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState from a JSON string
interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state_instance = InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state_dict = interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState from a dict
interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state_form_dict = interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state.from_dict(interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


