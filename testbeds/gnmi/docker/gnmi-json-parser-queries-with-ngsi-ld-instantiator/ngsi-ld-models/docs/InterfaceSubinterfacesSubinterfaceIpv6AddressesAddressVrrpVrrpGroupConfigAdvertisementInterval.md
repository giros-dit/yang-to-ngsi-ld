# InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigAdvertisementInterval

Sets the interval between successive VRRP advertisements -- RFC 5798 defines this as a 12-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second. Several implementation express this in units of seconds  Units: centiseconds  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **int** |  | [default to 100]
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval import InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigAdvertisementInterval

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigAdvertisementInterval from a JSON string
interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval_instance = InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigAdvertisementInterval.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigAdvertisementInterval.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval_dict = interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigAdvertisementInterval from a dict
interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval_form_dict = interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval.from_dict(interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_advertisement_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


