# InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup

List of VRRP groups, keyed by virtual router id  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup. | [default to 'InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**virtual_router_id** | [**InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupVirtualRouterId**](InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupVirtualRouterId.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group import InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup from a JSON string
interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_instance = InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_dict = interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup from a dict
interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_form_dict = interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group.from_dict(interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


