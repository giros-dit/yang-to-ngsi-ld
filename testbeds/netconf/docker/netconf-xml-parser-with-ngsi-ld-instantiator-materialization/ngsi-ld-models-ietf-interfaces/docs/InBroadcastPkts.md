# InBroadcastPkts

The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were addressed to a broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'discontinuity-time'.  Reference: RFC 2863: The Interfaces Group MIB -      ifHCInBroadcastPkts  YANG module: ietf-interfaces.yang 

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
from ngsi_ld_models_ietf_interfaces.models.in_broadcast_pkts import InBroadcastPkts

# TODO update the JSON string below
json = "{}"
# create an instance of InBroadcastPkts from a JSON string
in_broadcast_pkts_instance = InBroadcastPkts.from_json(json)
# print the JSON string representation of the object
print(InBroadcastPkts.to_json())

# convert the object into a dict
in_broadcast_pkts_dict = in_broadcast_pkts_instance.to_dict()
# create an instance of InBroadcastPkts from a dict
in_broadcast_pkts_from_dict = InBroadcastPkts.from_dict(in_broadcast_pkts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


