# InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig

Configuration data for each configured IPv4 address on the interface  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig. | [default to 'InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ip** | [**InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfigIp**](InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfigIp.md) |  | [optional] 
**prefix_length** | [**InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfigPrefixLength**](InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfigPrefixLength.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv4_addresses_address_config import InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig from a JSON string
interface_subinterfaces_subinterface_ipv4_addresses_address_config_instance = InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv4_addresses_address_config_dict = interface_subinterfaces_subinterface_ipv4_addresses_address_config_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig from a dict
interface_subinterfaces_subinterface_ipv4_addresses_address_config_form_dict = interface_subinterfaces_subinterface_ipv4_addresses_address_config.from_dict(interface_subinterfaces_subinterface_ipv4_addresses_address_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


