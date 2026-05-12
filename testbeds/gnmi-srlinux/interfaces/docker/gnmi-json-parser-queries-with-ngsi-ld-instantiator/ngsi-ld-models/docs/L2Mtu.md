# L2Mtu

Layer-2 MTU of the subinterface in bytes.  Includes the Ethernet header and VLAN tags, and excludes 4-bytes FCS.  L2 MTU specifies the maximum sized Ethernet frame that can be transmitted on the subinterface. If a frame exceeds this size it is discarded. If the l2-mtu of the subinterface exceeds the port-mtu of the associated interface, the subinterface will remain operationally down.  The default value for a subinterface is taken from /system/mtu/default-l2-mtu. The L2 MTU is only configurable for bridged subinterfaces.  The 7220 IXR-D1, 7220 IXR-D2, 7220 IXR-D3, 7220 IXR-H2, and 7220 IXR-H3 systems support a maximum L2 MTU of 9412 bytes and minimum of 1500 bytes.  The VSRL system supports a maximum L2 MTU of 9500 and minimum of 1450 bytes.  All other systems support a maximum L2 MTU of 9500 and minimum of 1500 bytes.  Units: bytes  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.l2_mtu import L2Mtu

# TODO update the JSON string below
json = "{}"
# create an instance of L2Mtu from a JSON string
l2_mtu_instance = L2Mtu.from_json(json)
# print the JSON string representation of the object
print L2Mtu.to_json()

# convert the object into a dict
l2_mtu_dict = l2_mtu_instance.to_dict()
# create an instance of L2Mtu from a dict
l2_mtu_form_dict = l2_mtu.from_dict(l2_mtu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


