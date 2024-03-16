# InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig

Configuration data for VRRP interface tracking  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig. | [default to 'InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**track_interface** | [**InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigTrackInterface**](InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigTrackInterface.md) |  | [optional] 
**priority_decrement** | [**InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement**](InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config import InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig from a JSON string
interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_instance = InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig.from_json(json)
# print the JSON string representation of the object
print InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig.to_json()

# convert the object into a dict
interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_dict = interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_instance.to_dict()
# create an instance of InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig from a dict
interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_form_dict = interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config.from_dict(interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


