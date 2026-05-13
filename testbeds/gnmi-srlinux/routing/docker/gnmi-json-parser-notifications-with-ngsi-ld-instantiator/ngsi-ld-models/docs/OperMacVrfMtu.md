# OperMacVrfMtu

Operational l2-mtu of the mac-vrf network-instance  Calculated as the lowest l2-mtu of the bridged subinterfaces associated to the mac-vrf, minus the associated vlan tags of the subinterface. The subinterface l2-mtu is the value configured under the subinterface, or the system/mtu/default-l2-mtu value otherwise. For mac-vrf network-instances without subinterfaces, the oper-mac-vrf-mtu matches the system/mtu/default-l2-mtu value.  When the mac-vrf has an associated irb subinterface, if the configured irb ip-mtu exceeds the oper-mac-vrf-mtu minus 14 bytes (Ethernet header), then the irb subinterface will remain operationally down.  The oper-mac-vrf-mtu is only available in mac-vrf network-instances.  Units: bytes  YANG module: srl_nokia-network-instance.yang 

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
from ngsi_ld_models.models.oper_mac_vrf_mtu import OperMacVrfMtu

# TODO update the JSON string below
json = "{}"
# create an instance of OperMacVrfMtu from a JSON string
oper_mac_vrf_mtu_instance = OperMacVrfMtu.from_json(json)
# print the JSON string representation of the object
print(OperMacVrfMtu.to_json())

# convert the object into a dict
oper_mac_vrf_mtu_dict = oper_mac_vrf_mtu_instance.to_dict()
# create an instance of OperMacVrfMtu from a dict
oper_mac_vrf_mtu_from_dict = OperMacVrfMtu.from_dict(oper_mac_vrf_mtu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


