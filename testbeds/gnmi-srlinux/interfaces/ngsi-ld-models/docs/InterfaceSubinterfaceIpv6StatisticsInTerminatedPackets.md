# InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets

The total number of input IPv4 packets or IPv6 packets or both that were received on this subinterface and that have a destination IP address matching a local interface address or an IPv6 multicast address to which the interface belongs. The count includes packets eventually discarded by the CPM. Such discards include: - packets with unsupported IP protocol numbers - packets destined to TCP/UDP ports that are not open/listening - IPv4 packets with any IP options - IPv6 packets with any extension headers  This also includes terminating IP/MPLS packets.  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **int** |  | 
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
from ngsi_ld_models.models.interface_subinterface_ipv6_statistics_in_terminated_packets import InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets from a JSON string
interface_subinterface_ipv6_statistics_in_terminated_packets_instance = InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets.to_json()

# convert the object into a dict
interface_subinterface_ipv6_statistics_in_terminated_packets_dict = interface_subinterface_ipv6_statistics_in_terminated_packets_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets from a dict
interface_subinterface_ipv6_statistics_in_terminated_packets_form_dict = interface_subinterface_ipv6_statistics_in_terminated_packets.from_dict(interface_subinterface_ipv6_statistics_in_terminated_packets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


