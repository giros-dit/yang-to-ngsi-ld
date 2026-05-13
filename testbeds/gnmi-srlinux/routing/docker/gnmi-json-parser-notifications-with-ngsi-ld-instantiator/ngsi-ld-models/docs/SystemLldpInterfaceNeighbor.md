# SystemLldpInterfaceNeighbor

List of LLDP neighbors on this interface  YANG module: srl_nokia-lldp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**SystemLldpInterfaceNeighborId**](SystemLldpInterfaceNeighborId.md) |  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SystemLldpInterfaceNeighbor. | [default to 'SystemLldpInterfaceNeighbor']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**first_message** | [**FirstMessage**](FirstMessage.md) |  | [optional] 
**last_update** | [**LastUpdate**](LastUpdate.md) |  | [optional] 
**system_name** | [**SystemLldpInterfaceNeighborSystemName**](SystemLldpInterfaceNeighborSystemName.md) |  | [optional] 
**system_description** | [**SystemLldpInterfaceNeighborSystemDescription**](SystemLldpInterfaceNeighborSystemDescription.md) |  | [optional] 
**chassis_id** | [**SystemLldpInterfaceNeighborChassisId**](SystemLldpInterfaceNeighborChassisId.md) |  | [optional] 
**chassis_id_type** | [**SystemLldpInterfaceNeighborChassisIdType**](SystemLldpInterfaceNeighborChassisIdType.md) |  | [optional] 
**port_id** | [**PortId**](PortId.md) |  | [optional] 
**port_id_type** | [**PortIdType**](PortIdType.md) |  | [optional] 
**port_description** | [**PortDescription**](PortDescription.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.system_lldp_interface_neighbor import SystemLldpInterfaceNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLldpInterfaceNeighbor from a JSON string
system_lldp_interface_neighbor_instance = SystemLldpInterfaceNeighbor.from_json(json)
# print the JSON string representation of the object
print(SystemLldpInterfaceNeighbor.to_json())

# convert the object into a dict
system_lldp_interface_neighbor_dict = system_lldp_interface_neighbor_instance.to_dict()
# create an instance of SystemLldpInterfaceNeighbor from a dict
system_lldp_interface_neighbor_from_dict = SystemLldpInterfaceNeighbor.from_dict(system_lldp_interface_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


