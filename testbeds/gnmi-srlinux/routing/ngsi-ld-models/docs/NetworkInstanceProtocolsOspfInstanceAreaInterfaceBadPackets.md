# NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets

Bad packets counters  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**bad_version** | [**BadVersion**](BadVersion.md) |  | [optional] 
**bad_network** | [**BadNetwork**](BadNetwork.md) |  | [optional] 
**bad_area** | [**BadArea**](BadArea.md) |  | [optional] 
**bad_dest_address** | [**BadDestAddress**](BadDestAddress.md) |  | [optional] 
**bad_neighbors** | [**BadNeighbors**](BadNeighbors.md) |  | [optional] 
**bad_packet_type** | [**BadPacketType**](BadPacketType.md) |  | [optional] 
**bad_length** | [**BadLength**](BadLength.md) |  | [optional] 
**bad_hello_interval** | [**BadHelloInterval**](BadHelloInterval.md) |  | [optional] 
**bad_dead_interval** | [**BadDeadInterval**](BadDeadInterval.md) |  | [optional] 
**bad_options** | [**BadOptions**](BadOptions.md) |  | [optional] 
**bad_checksum** | [**BadChecksum**](BadChecksum.md) |  | [optional] 
**bad_auth_type** | [**BadAuthType**](BadAuthType.md) |  | [optional] 
**auth_failures** | [**AuthFailures**](AuthFailures.md) |  | [optional] 
**bad_virtual_link** | [**BadVirtualLink**](BadVirtualLink.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_interface_bad_packets import NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets from a JSON string
network_instance_protocols_ospf_instance_area_interface_bad_packets_instance = NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_interface_bad_packets_dict = network_instance_protocols_ospf_instance_area_interface_bad_packets_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets from a dict
network_instance_protocols_ospf_instance_area_interface_bad_packets_from_dict = NetworkInstanceProtocolsOspfInstanceAreaInterfaceBadPackets.from_dict(network_instance_protocols_ospf_instance_area_interface_bad_packets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


