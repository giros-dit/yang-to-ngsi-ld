# NetworkInstanceRouteTableNextHopTunnelIpInIp

Specifies details of the IP-in-IP header added to the packet. This is provided only when encapsulate-header is ipv4 or ipv6  YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableNextHopTunnelIpInIp. | [default to 'NetworkInstanceRouteTableNextHopTunnelIpInIp']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**src_ip** | [**SrcIp**](SrcIp.md) |  | [optional] 
**dst_ip** | [**DstIp**](DstIp.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_next_hop_tunnel_ip_in_ip import NetworkInstanceRouteTableNextHopTunnelIpInIp

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableNextHopTunnelIpInIp from a JSON string
network_instance_route_table_next_hop_tunnel_ip_in_ip_instance = NetworkInstanceRouteTableNextHopTunnelIpInIp.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableNextHopTunnelIpInIp.to_json())

# convert the object into a dict
network_instance_route_table_next_hop_tunnel_ip_in_ip_dict = network_instance_route_table_next_hop_tunnel_ip_in_ip_instance.to_dict()
# create an instance of NetworkInstanceRouteTableNextHopTunnelIpInIp from a dict
network_instance_route_table_next_hop_tunnel_ip_in_ip_from_dict = NetworkInstanceRouteTableNextHopTunnelIpInIp.from_dict(network_instance_route_table_next_hop_tunnel_ip_in_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


