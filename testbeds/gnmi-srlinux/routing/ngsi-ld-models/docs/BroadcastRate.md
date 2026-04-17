# BroadcastRate

The maximum rate allowed for ingress broadcast frames on the interface  The rate can be set in multiple of 64kbps. If the rate is configured to any value in the 1-127 kbps range, the effective rate will be 64kbps and shown in the operational rate. If any value in the 128-191 range, the effective rate will be 128kbps and shown in the operational rate, and so on for higher rates. When the rate is set to zero, all the broadcast traffic in the interface is discarded.  The maximum rate that can be effectively configured in 7220 D4/D5 platforms is 132000000. When a configured percentage exceeds that value, the maximum supported rate is set and shown in the operational-broadcast-rate.  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.broadcast_rate import BroadcastRate

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastRate from a JSON string
broadcast_rate_instance = BroadcastRate.from_json(json)
# print the JSON string representation of the object
print(BroadcastRate.to_json())

# convert the object into a dict
broadcast_rate_dict = broadcast_rate_instance.to_dict()
# create an instance of BroadcastRate from a dict
broadcast_rate_from_dict = BroadcastRate.from_dict(broadcast_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


