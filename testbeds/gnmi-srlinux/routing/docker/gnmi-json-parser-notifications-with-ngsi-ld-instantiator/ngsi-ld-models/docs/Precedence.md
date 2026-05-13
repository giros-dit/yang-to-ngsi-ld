# Precedence

The precedence value of the pseudowire within the connection point  The precedence value is used to select the (only) pseudowire that transmits traffic in the connection-point (referred to as primary pseudowire). After removing from consideration all the pseudowires that are operationally down or receive T-LDP pseudowire status signaling different from 'pseudowire-forwarding' (all the bits set to zero), the pseudowire with the lowest precedence value is selected as active to transmit traffic in the connection-point. The value 'primary' is considered lower than any of the numerical values ('primary' is equivalent to value '0'), with value '4' being the highest value.  The router forces the user to configure different precedence values for the pseudowires in the connection-point. The selected primary pseudowire is used to transmit traffic and the router only switches to another secondary pseudowire when the primary is down. The connection-point switches the path back to the primary pseudowire when it is back up, unless the connection-point is configured with 'revert-time never'.  YANG module: srl_nokia-network-instance.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
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
from ngsi_ld_models.models.precedence import Precedence

# TODO update the JSON string below
json = "{}"
# create an instance of Precedence from a JSON string
precedence_instance = Precedence.from_json(json)
# print the JSON string representation of the object
print(Precedence.to_json())

# convert the object into a dict
precedence_dict = precedence_instance.to_dict()
# create an instance of Precedence from a dict
precedence_from_dict = Precedence.from_dict(precedence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


