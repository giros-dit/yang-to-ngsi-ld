# ReplaceAttrsRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**type** | **str** | Node type.  | [optional] [default to 'ListRelationship']
**value** | [**Geometry**](Geometry.md) |  | [optional] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a ListRelationship instance as mandated by clause 4.5.8. System generated. Only used in temporal representation of ListRelationships.  | [optional] [readonly] 
**previous_value** | [**Geometry**](Geometry.md) |  | [optional] 
**object** | [**RelationshipObject**](RelationshipObject.md) |  | [optional] 
**object_type** | [**RelationshipObjectType**](RelationshipObjectType.md) |  | [optional] 
**previous_object** | [**RelationshipPreviousObject**](RelationshipPreviousObject.md) |  | [optional] 
**entity** | [**RelationshipEntity**](RelationshipEntity.md) |  | [optional] 
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 
**previous_language_map** | **object** | Previous LanguageProperty&#39;s languageMap. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 
**vocab** | [**VocabPropertyVocab**](VocabPropertyVocab.md) |  | [optional] 
**previous_vocab** | [**VocabPropertyPreviousVocab**](VocabPropertyPreviousVocab.md) |  | [optional] 
**var_json** | **object** | Raw unexpandable JSON which shall not be interpreted as JSON-LD using the supplied @context.  | [optional] 
**previous_json** | **object** | Previous JsonProperty&#39;s json. Only used in notifications, if the showChanges  option is explicitly requested.  | [optional] [readonly] 
**value_list** | [**List[ListPropertyValueListInner]**](ListPropertyValueListInner.md) | Ordered array of Property Values.  | [optional] 
**previous_value_list** | [**List[ListPropertyValueListInner]**](ListPropertyValueListInner.md) | Ordered array of Property Values. See NGSI-LD Value definition in clause 3.1  | [optional] [readonly] 
**object_list** | [**ListRelationshipObjectList**](ListRelationshipObjectList.md) |  | [optional] 
**previous_object_list** | [**ListRelationshipPreviousObjectList**](ListRelationshipPreviousObjectList.md) |  | [optional] 
**entity_list** | [**List[Entity]**](Entity.md) | An array of inline Entity obtained by Linked Entity Retrieval, corresponding  to the ListRelationship&#39;s target object. See clause 4.5.23.2. Only used in  Linked Entity Retrieval, if the join&#x3D;inline option is explicitly requested.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models_1_8_1.models.replace_attrs_request1 import ReplaceAttrsRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceAttrsRequest1 from a JSON string
replace_attrs_request1_instance = ReplaceAttrsRequest1.from_json(json)
# print the JSON string representation of the object
print(ReplaceAttrsRequest1.to_json())

# convert the object into a dict
replace_attrs_request1_dict = replace_attrs_request1_instance.to_dict()
# create an instance of ReplaceAttrsRequest1 from a dict
replace_attrs_request1_from_dict = ReplaceAttrsRequest1.from_dict(replace_attrs_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


