# InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfigMode

When set to a value other than DISABLE, the local system should respond to ARP requests that are for target addresses other than those that are configured on the local subinterface using its own MAC address as the target hardware address. If the REMOTE_ONLY value is specified, replies are only sent when the target address falls outside the locally configured subnets on the interface, whereas with the ALL value, all requests, regardless of their target address are replied to.  Reference: RFC1027: Using ARP to Implement Transparent Subnet Gateways  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | [default to 'DISABLE']
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
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode import InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfigMode

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfigMode from a JSON string
interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode_instance = InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfigMode.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfigMode.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode_dict = interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfigMode from a dict
interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode_form_dict = interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode.from_dict(interface_subinterfaces_subinterface_ipv4_proxy_arp_config_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


