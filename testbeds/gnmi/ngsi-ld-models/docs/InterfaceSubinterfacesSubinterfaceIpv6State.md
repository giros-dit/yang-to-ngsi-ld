# InterfaceSubinterfacesSubinterfaceIpv6State

Top-level operational state data for the IPv6 interface  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv6State. | [default to 'InterfaceSubinterfacesSubinterfaceIpv6State']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**enabled** | [**InterfaceSubinterfacesSubinterfaceIpv6StateEnabled**](InterfaceSubinterfacesSubinterfaceIpv6StateEnabled.md) |  | [optional] 
**mtu** | [**InterfaceSubinterfacesSubinterfaceIpv6StateMtu**](InterfaceSubinterfacesSubinterfaceIpv6StateMtu.md) |  | [optional] 
**dup_addr_detect_transmits** | [**InterfaceSubinterfacesSubinterfaceIpv6StateDupAddrDetectTransmits**](InterfaceSubinterfacesSubinterfaceIpv6StateDupAddrDetectTransmits.md) |  | [optional] 
**dhcp_client** | [**InterfaceSubinterfacesSubinterfaceIpv6StateDhcpClient**](InterfaceSubinterfacesSubinterfaceIpv6StateDhcpClient.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv6_state import InterfaceSubinterfacesSubinterfaceIpv6State

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6State from a JSON string
interface_subinterfaces_subinterface_ipv6_state_instance = InterfaceSubinterfacesSubinterfaceIpv6State.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv6State.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv6_state_dict = interface_subinterfaces_subinterface_ipv6_state_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6State from a dict
interface_subinterfaces_subinterface_ipv6_state_form_dict = interface_subinterfaces_subinterface_ipv6_state.from_dict(interface_subinterfaces_subinterface_ipv6_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

