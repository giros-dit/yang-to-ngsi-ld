# InterfaceSubinterfaceIpv4Address

The list of IPv4 addresses assigned to the subinterface.  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfaceIpv4Address. | [default to 'InterfaceSubinterfaceIpv4Address']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ip_prefix** | [**InterfaceSubinterfaceIpv4AddressIpPrefix**](InterfaceSubinterfaceIpv4AddressIpPrefix.md) |  | [optional] 
**anycast_gw** | [**InterfaceSubinterfaceIpv4AddressAnycastGw**](InterfaceSubinterfaceIpv4AddressAnycastGw.md) |  | [optional] 
**origin** | [**InterfaceSubinterfaceIpv4AddressOrigin**](InterfaceSubinterfaceIpv4AddressOrigin.md) |  | [optional] 
**primary** | [**InterfaceSubinterfaceIpv4AddressPrimary**](InterfaceSubinterfaceIpv4AddressPrimary.md) |  | [optional] 
**status** | [**InterfaceSubinterfaceIpv4AddressStatus**](InterfaceSubinterfaceIpv4AddressStatus.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterface_ipv4_address import InterfaceSubinterfaceIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv4Address from a JSON string
interface_subinterface_ipv4_address_instance = InterfaceSubinterfaceIpv4Address.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv4Address.to_json()

# convert the object into a dict
interface_subinterface_ipv4_address_dict = interface_subinterface_ipv4_address_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv4Address from a dict
interface_subinterface_ipv4_address_form_dict = interface_subinterface_ipv4_address.from_dict(interface_subinterface_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


