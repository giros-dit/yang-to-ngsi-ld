# AllowDirectedBroadcast

When this is set to true the software is allowed to re-broadcast targeted broadcast IPv4 packets on this subinterface  Detailed handling of subnet broadcast is as follows:  If a targeted broadcast packet is received on subinterface X that has the matching subnet then it is delivered to the CPM and CPM will reply to an ICMP echo.  If a targeted broadcast packet is received on subinterface X but the matching subnet is associated with subinterface Y, and subinterface Y is configured with allow-directed-broadcasts=false then it is delivered to the CPM and CPM replies to an ICMP echo per above, but it does not re-broadcast the packet on subinterface Y.  If a targeted broadcast packet is received on subinterface X but the matching subnet is associated with subinterface Y, and subinterface Y is configured with allow-directed-broadcasts=true then it is delivered to the CPM and CPM replies to an ICMP echo per above, and CPM also re-broadcasts the packet on subinterface Y.  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **bool** |  | [default to False]
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
from ngsi_ld_models.models.allow_directed_broadcast import AllowDirectedBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of AllowDirectedBroadcast from a JSON string
allow_directed_broadcast_instance = AllowDirectedBroadcast.from_json(json)
# print the JSON string representation of the object
print AllowDirectedBroadcast.to_json()

# convert the object into a dict
allow_directed_broadcast_dict = allow_directed_broadcast_instance.to_dict()
# create an instance of AllowDirectedBroadcast from a dict
allow_directed_broadcast_form_dict = allow_directed_broadcast.from_dict(allow_directed_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


