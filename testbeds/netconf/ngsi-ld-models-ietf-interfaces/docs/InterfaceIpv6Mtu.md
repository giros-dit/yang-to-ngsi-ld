# InterfaceIpv6Mtu

The size, in octets, of the largest IPv6 packet that the interface will send and receive.  Reference: RFC 2460: Internet Protocol, Version 6 (IPv6) Specification      Section 5  Units: octets  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **int** |  | 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance as  mandated by clause 4.5.7. System generated. Only used in temporal representation of Properties.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_ipv6_mtu import InterfaceIpv6Mtu

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceIpv6Mtu from a JSON string
interface_ipv6_mtu_instance = InterfaceIpv6Mtu.from_json(json)
# print the JSON string representation of the object
print(InterfaceIpv6Mtu.to_json())

# convert the object into a dict
interface_ipv6_mtu_dict = interface_ipv6_mtu_instance.to_dict()
# create an instance of InterfaceIpv6Mtu from a dict
interface_ipv6_mtu_from_dict = InterfaceIpv6Mtu.from_dict(interface_ipv6_mtu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


