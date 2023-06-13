# HigherLayerIf

NGSI-LD Relationship Type. A list of references to interfaces layered on top of this interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**object** | **str** | Relationship&#39;s target object.  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated.  | [optional] 

## Example

```python
from ngsi_ld_models.models.higher_layer_if import HigherLayerIf

# TODO update the JSON string below
json = "{}"
# create an instance of HigherLayerIf from a JSON string
higher_layer_if_instance = HigherLayerIf.from_json(json)
# print the JSON string representation of the object
print HigherLayerIf.to_json()

# convert the object into a dict
higher_layer_if_dict = higher_layer_if_instance.to_dict()
# create an instance of HigherLayerIf from a dict
higher_layer_if_form_dict = higher_layer_if.from_dict(higher_layer_if_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


