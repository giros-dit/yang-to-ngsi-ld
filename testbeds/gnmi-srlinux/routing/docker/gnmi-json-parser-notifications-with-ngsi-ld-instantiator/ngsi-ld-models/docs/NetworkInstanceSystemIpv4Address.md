# NetworkInstanceSystemIpv4Address

Container for displaying information about the system IPv4 address of the default network-instance  YANG module: srl_nokia-network-instance.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceSystemIpv4Address. | [default to 'NetworkInstanceSystemIpv4Address']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**oper_state** | [**NetworkInstanceSystemIpv4AddressOperState**](NetworkInstanceSystemIpv4AddressOperState.md) |  | [optional] 
**oper_down_reason** | [**NetworkInstanceSystemIpv4AddressOperDownReason**](NetworkInstanceSystemIpv4AddressOperDownReason.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_system_ipv4_address import NetworkInstanceSystemIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceSystemIpv4Address from a JSON string
network_instance_system_ipv4_address_instance = NetworkInstanceSystemIpv4Address.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceSystemIpv4Address.to_json())

# convert the object into a dict
network_instance_system_ipv4_address_dict = network_instance_system_ipv4_address_instance.to_dict()
# create an instance of NetworkInstanceSystemIpv4Address from a dict
network_instance_system_ipv4_address_from_dict = NetworkInstanceSystemIpv4Address.from_dict(network_instance_system_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


