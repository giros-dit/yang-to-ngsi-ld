# InterfaceMtu

Port MTU in bytes including ethernet overhead but excluding 4-bytes FCS  If a transmitted packet exceeds this size it is dropped. The default value for ethernet-x interfaces is taken from /system/mtu/default-port-mtu. For the mgmt0 and mgmt0-standby interfaces the default is 1514 bytes, but the value can be changed for each interface individually. For the mgmtA and mgmtB interfaces the default value is derived from mgmt0 or mgmt0-standby configuration. Port MTU is not configurable for loopback interfaces or irb interfaces. For irb interfaces, if the size of the ip packets to be routed to a mac-vrf has to be restricted, the subinterface.ip-mtu should be configured instead. The max mtu for the mgmt0, mgmt0-standby, mgmtA and mgmtB interfaces is 9216. The 7220 IXR systems support a maximum port MTU of 9412 bytes and minimum of 1500 bytes. The VSRL system supports a maximum port MTU of 9500 and minimum of 1450 bytes. The 7730 SXR systems support a maximum port MTU of 9408 bytes and minimum of 1500 bytes. All other systems support a maximum port MTU of 9500 and minimum of 1500 bytes. Each 7250 IXR IMM supports a maximum of 8 different port MTU values. 7220 IXR systems do not have any limit on the maximum number of different port MTU values.  Units: bytes  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.interface_mtu import InterfaceMtu

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceMtu from a JSON string
interface_mtu_instance = InterfaceMtu.from_json(json)
# print the JSON string representation of the object
print(InterfaceMtu.to_json())

# convert the object into a dict
interface_mtu_dict = interface_mtu_instance.to_dict()
# create an instance of InterfaceMtu from a dict
interface_mtu_from_dict = InterfaceMtu.from_dict(interface_mtu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


