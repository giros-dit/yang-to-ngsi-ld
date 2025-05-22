# InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig

Configuration parameters relating to router advertisements for IPv6.  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig. | [default to 'InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**interval** | [**InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfigInterval**](InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfigInterval.md) |  | [optional] 
**lifetime** | [**InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfigLifetime**](InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfigLifetime.md) |  | [optional] 
**suppress** | [**InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfigSuppress**](InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfigSuppress.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv6_router_advertisement_config import InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig from a JSON string
interface_subinterfaces_subinterface_ipv6_router_advertisement_config_instance = InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv6_router_advertisement_config_dict = interface_subinterfaces_subinterface_ipv6_router_advertisement_config_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig from a dict
interface_subinterfaces_subinterface_ipv6_router_advertisement_config_form_dict = interface_subinterfaces_subinterface_ipv6_router_advertisement_config.from_dict(interface_subinterfaces_subinterface_ipv6_router_advertisement_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


