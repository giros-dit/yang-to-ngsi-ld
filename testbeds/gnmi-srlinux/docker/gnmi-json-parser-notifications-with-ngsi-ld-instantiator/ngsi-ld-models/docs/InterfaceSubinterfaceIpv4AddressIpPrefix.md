# InterfaceSubinterfaceIpv4AddressIpPrefix

The IPv4 address and prefix length in CIDR notation  Subnets on the same subinterface are allowed to overlap as long as the host bits are different. When a locally originated unicast packet is destined to a host covered by multiple subnets associated with a subinterface, the source address is chosen to be the numerically lowest IP address among all these subnets. For example, if the addresses 172.16.1.1/12, 172.16.1.2/12, and 172.16.1.3/12 are configured on the same interface, 172.16.1.1 would be used as a local address when you issue a ping 172.16.1.5 command  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
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
from ngsi_ld_models.models.interface_subinterface_ipv4_address_ip_prefix import InterfaceSubinterfaceIpv4AddressIpPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv4AddressIpPrefix from a JSON string
interface_subinterface_ipv4_address_ip_prefix_instance = InterfaceSubinterfaceIpv4AddressIpPrefix.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv4AddressIpPrefix.to_json()

# convert the object into a dict
interface_subinterface_ipv4_address_ip_prefix_dict = interface_subinterface_ipv4_address_ip_prefix_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv4AddressIpPrefix from a dict
interface_subinterface_ipv4_address_ip_prefix_form_dict = interface_subinterface_ipv4_address_ip_prefix.from_dict(interface_subinterface_ipv4_address_ip_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


