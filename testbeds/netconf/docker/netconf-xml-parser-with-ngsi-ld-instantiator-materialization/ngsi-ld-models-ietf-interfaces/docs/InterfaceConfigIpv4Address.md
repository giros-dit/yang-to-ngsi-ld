# InterfaceConfigIpv4Address

The list of configured IPv4 addresses on the interface.  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceConfigIpv4Address. | [default to 'InterfaceConfigIpv4Address']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**ip** | [**InterfaceConfigIpv4AddressIp**](InterfaceConfigIpv4AddressIp.md) |  | [optional] 
**prefix_length** | [**InterfaceIpv4AddressSubnetPrefixLength**](InterfaceIpv4AddressSubnetPrefixLength.md) |  | [optional] 
**netmask** | [**InterfaceIpv4AddressSubnetNetmask**](InterfaceIpv4AddressSubnetNetmask.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4_address import InterfaceConfigIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfigIpv4Address from a JSON string
interface_config_ipv4_address_instance = InterfaceConfigIpv4Address.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfigIpv4Address.to_json())

# convert the object into a dict
interface_config_ipv4_address_dict = interface_config_ipv4_address_instance.to_dict()
# create an instance of InterfaceConfigIpv4Address from a dict
interface_config_ipv4_address_from_dict = InterfaceConfigIpv4Address.from_dict(interface_config_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


