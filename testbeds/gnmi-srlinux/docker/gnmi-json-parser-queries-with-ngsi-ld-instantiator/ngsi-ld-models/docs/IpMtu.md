# IpMtu

IP MTU of the subinterface in bytes.  Includes the IP header but excludes Ethernet encapsulation.  IP MTU specifies the maximum sized IPv4 or IPv6 packet that can be transmitted on the subinterface. If an IPv4 or IPv6 packet exceeds this size it is dropped and this may result in the generation of an ICMP error message back to the source.  The default IP MTU for a subinterface is taken from /system/mtu/default-ip-mtu. For the mgmt0 and mgmt0-standby subinterfaces the default is the associated interface MTU minus the Ethernet encapsulation overhead.  The IP MTU is not configurable for subinterfaces of loopback interfaces.  The 7220 IXR-D1, 7220 IXR-D2, 7220 IXR-D3, 7220 IXR-H2, and 7220 IXR-H3 systems support a maximum IP MTU of 9398 bytes.  Each 7250 IXR IMM supports a maximum of 4 different IP MTU values. 7220 IXR systems do not have any limit on the maximum number of different IP MTU values.  Units: bytes  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.ip_mtu import IpMtu

# TODO update the JSON string below
json = "{}"
# create an instance of IpMtu from a JSON string
ip_mtu_instance = IpMtu.from_json(json)
# print the JSON string representation of the object
print IpMtu.to_json()

# convert the object into a dict
ip_mtu_dict = ip_mtu_instance.to_dict()
# create an instance of IpMtu from a dict
ip_mtu_form_dict = ip_mtu.from_dict(ip_mtu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


