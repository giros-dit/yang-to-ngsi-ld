# LanguageProperty

5.2.32 NGSI-LD LanguageProperty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'LanguageProperty']
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a LanguageProperty instance, as mandated by clause 4.5.7. System generated. Only used in temporal representation of LanguageProperties.  | [optional] [readonly] 
**previous_language_map** | **object** | Previous LanguageProperty&#39;s languageMap. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models_1_8_1.models.language_property import LanguageProperty

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageProperty from a JSON string
language_property_instance = LanguageProperty.from_json(json)
# print the JSON string representation of the object
print(LanguageProperty.to_json())

# convert the object into a dict
language_property_dict = language_property_instance.to_dict()
# create an instance of LanguageProperty from a dict
language_property_from_dict = LanguageProperty.from_dict(language_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

