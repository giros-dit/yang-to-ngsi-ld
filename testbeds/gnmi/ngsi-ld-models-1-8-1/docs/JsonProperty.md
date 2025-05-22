# JsonProperty

5.2.38 NGSI-LD JsonProperty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'JsonProperty']
**var_json** | **object** | Raw unexpandable JSON which shall not be interpreted as JSON-LD using the supplied @context.  | [optional] 
**previous_json** | **object** | Previous JsonProperty&#39;s json. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a JsonProperty instance, as mandated by clause 4.5.7. System generated. Only used in temporal representation of JsonProperties.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models_1_8_1.models.json_property import JsonProperty

# TODO update the JSON string below
json = "{}"
# create an instance of JsonProperty from a JSON string
json_property_instance = JsonProperty.from_json(json)
# print the JSON string representation of the object
print(JsonProperty.to_json())

# convert the object into a dict
json_property_dict = json_property_instance.to_dict()
# create an instance of JsonProperty from a dict
json_property_from_dict = JsonProperty.from_dict(json_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


