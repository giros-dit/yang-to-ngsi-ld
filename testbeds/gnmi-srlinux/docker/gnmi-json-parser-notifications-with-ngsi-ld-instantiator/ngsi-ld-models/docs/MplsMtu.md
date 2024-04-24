# MplsMtu

MPLS MTU of the subinterface in bytes, including the transmitted label stack.  MPLS MTU specifies the maximum sized MPLS packet that can be transmitted on the subinterface. If an MPLS packet containing any payload exceeds this size then it is dropped. If the payload of the dropped packet is IPv4 or IPv6 then this may also result in the generation of an ICMP error message that is either tunneled or sent back to the source.  The default MPLS MTU for a subinterface is taken from /system/mtu/default-mpls-mtu.  The MPLS MTU is not configurable for subinterfaces of loopback interfaces.  Each 7250 IXR IMM supports a maximum of 4 different MPLS MTU values.  Units: bytes  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.mpls_mtu import MplsMtu

# TODO update the JSON string below
json = "{}"
# create an instance of MplsMtu from a JSON string
mpls_mtu_instance = MplsMtu.from_json(json)
# print the JSON string representation of the object
print MplsMtu.to_json()

# convert the object into a dict
mpls_mtu_dict = mpls_mtu_instance.to_dict()
# create an instance of MplsMtu from a dict
mpls_mtu_form_dict = mpls_mtu.from_dict(mpls_mtu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


