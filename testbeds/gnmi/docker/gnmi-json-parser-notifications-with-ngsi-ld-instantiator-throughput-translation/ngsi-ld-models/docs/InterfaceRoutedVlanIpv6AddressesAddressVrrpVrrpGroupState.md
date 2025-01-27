# InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState

Operational state data for the VRRP group  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState. | [default to 'InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**virtual_router_id** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateVirtualRouterId**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateVirtualRouterId.md) |  | [optional] 
**virtual_address** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateVirtualAddress**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateVirtualAddress.md) |  | [optional] 
**priority** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStatePriority**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStatePriority.md) |  | [optional] 
**preempt** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStatePreempt**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStatePreempt.md) |  | [optional] 
**preempt_delay** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStatePreemptDelay**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStatePreemptDelay.md) |  | [optional] 
**accept_mode** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateAcceptMode**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateAcceptMode.md) |  | [optional] 
**advertisement_interval** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateAdvertisementInterval**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateAdvertisementInterval.md) |  | [optional] 
**current_priority** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateCurrentPriority**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateCurrentPriority.md) |  | [optional] 
**virtual_link_local** | [**InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateVirtualLinkLocal**](InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupStateVirtualLinkLocal.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state import InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState from a JSON string
interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state_instance = InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState.from_json(json)
# print the JSON string representation of the object
print InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState.to_json()

# convert the object into a dict
interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state_dict = interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state_instance.to_dict()
# create an instance of InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState from a dict
interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state_form_dict = interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state.from_dict(interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


