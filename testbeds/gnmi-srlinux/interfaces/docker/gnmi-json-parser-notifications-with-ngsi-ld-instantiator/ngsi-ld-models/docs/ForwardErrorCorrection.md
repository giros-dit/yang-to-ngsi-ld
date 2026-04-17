# ForwardErrorCorrection

The forward error correction algorithm to use on the optical channel  The same FEC algorithm must be used at both ends of a link.  25G interfaces support disabled, base-r rs-108 and rs-528; configuring other (incompatible) options will bring the port down. The FEC requirement for a 25G interface depends on the cable type. A CA-N DAC cable has a loss specification that requires no FEC. A CA-S DAC cable requires base-r FEC at a minimum. A CA-L DAC cable requires the stronger rs-108 Reed Solomon FEC.  100G interfaces support disabled and rs-528; configuring other (incompatible) options will bring the port down.  400G interfaces require rs-544; configuring other (unsupported) options will bring the port down.  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.forward_error_correction import ForwardErrorCorrection

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardErrorCorrection from a JSON string
forward_error_correction_instance = ForwardErrorCorrection.from_json(json)
# print the JSON string representation of the object
print ForwardErrorCorrection.to_json()

# convert the object into a dict
forward_error_correction_dict = forward_error_correction_instance.to_dict()
# create an instance of ForwardErrorCorrection from a dict
forward_error_correction_form_dict = forward_error_correction.from_dict(forward_error_correction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


