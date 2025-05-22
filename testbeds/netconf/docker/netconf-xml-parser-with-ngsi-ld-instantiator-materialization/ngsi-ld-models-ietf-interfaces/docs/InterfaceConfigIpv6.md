# InterfaceConfigIpv6

Parameters for the IPv6 address family.  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceConfigIpv6. | [default to 'InterfaceConfigIpv6']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**enabled** | [**InterfaceConfigIpv6Enabled**](InterfaceConfigIpv6Enabled.md) |  | [optional] 
**forwarding** | [**InterfaceConfigIpv6Forwarding**](InterfaceConfigIpv6Forwarding.md) |  | [optional] 
**mtu** | [**InterfaceConfigIpv6Mtu**](InterfaceConfigIpv6Mtu.md) |  | [optional] 
**dup_addr_detect_transmits** | [**DupAddrDetectTransmits**](DupAddrDetectTransmits.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6 import InterfaceConfigIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfigIpv6 from a JSON string
interface_config_ipv6_instance = InterfaceConfigIpv6.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfigIpv6.to_json())

# convert the object into a dict
interface_config_ipv6_dict = interface_config_ipv6_instance.to_dict()
# create an instance of InterfaceConfigIpv6 from a dict
interface_config_ipv6_from_dict = InterfaceConfigIpv6.from_dict(interface_config_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


