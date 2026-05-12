# InterfaceSubinterfaceIpv6AddressAnycastGw

This designates the associated IPv6 address as an anycast-gateway IPv6 address of the subinterface.  When this parameter is set to true: - The IPv6 address is associated with the anycast-gw MAC address in the same subinterface. Neighbor Solicitations received for the anycast-gw IPv6 address  will be replied using this anycast-gw MAC address. - The IPv6 address can have duplicate IPv6 addresses in other IRB subinterfaces of routers attached to the same broadcast domain.  Because of that, ND duplicate-address-detection procedures do not apply to anycast-gw IP addresses.  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **bool** |  | 
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
from ngsi_ld_models.models.interface_subinterface_ipv6_address_anycast_gw import InterfaceSubinterfaceIpv6AddressAnycastGw

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv6AddressAnycastGw from a JSON string
interface_subinterface_ipv6_address_anycast_gw_instance = InterfaceSubinterfaceIpv6AddressAnycastGw.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv6AddressAnycastGw.to_json()

# convert the object into a dict
interface_subinterface_ipv6_address_anycast_gw_dict = interface_subinterface_ipv6_address_anycast_gw_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv6AddressAnycastGw from a dict
interface_subinterface_ipv6_address_anycast_gw_form_dict = interface_subinterface_ipv6_address_anycast_gw.from_dict(interface_subinterface_ipv6_address_anycast_gw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


