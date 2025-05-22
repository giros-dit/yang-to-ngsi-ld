# QueryBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | JSON-LD @type.  | 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved.  | [optional] 
**attrs** | **List[str]** | List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved. A synonym for a combination of the pick and q parameter. DEPRECATED.  | [optional] 
**pick** | **List[str]** | When defined, every Entity within payload body is reduced down to only contain  the specified Entity members. Entity member (\&quot;id\&quot;, \&quot;type\&quot;, \&quot;scope\&quot; or a projected Attribute name) as a valid  attribute projection language string as per clause 4.21).  | [optional] 
**omit** | **List[str]** | When defined, the specified Entity members are removed from each Entity within  the payload. Entity member (\&quot;id\&quot;, \&quot;type\&quot;, \&quot;scope\&quot; or a projected Attribute name)  as a valid attribute projection language string as per clause 4.21).  | [optional] 
**q** | **str** | Query that shall be matched by Entities in order to be retrieved.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) |  | [optional] 
**csf** | **str** | Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities.  | [optional] 
**scope_q** | **str** | Scope query. | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15). | [optional] 
**contained_by** | **List[str]** | List of entity ids which have previously been encountered whilst retrieving the Entity Graph.  Only applicable if joinLevel is present.  Only applicable for the \&quot;Query Entities\&quot; operation (clause 5.7.2).  | [optional] 
**dataset_id** | **List[str]** | Specifies the datasetIds of the Attribute instances to be selected for each  matched Attribute as per clause 4.5.5. Valid URIs, \&quot;@none\&quot; for including the  default Attribute instances.  | [optional] 
**entity_map** | **bool** | If true, the location of the EntityMap used in the operation is returned in the response.  Only applicable for the \&quot;Query Entities\&quot; operation (clause 5.7.2).  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_client_1_8_1.models.query_batch_request import QueryBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBatchRequest from a JSON string
query_batch_request_instance = QueryBatchRequest.from_json(json)
# print the JSON string representation of the object
print(QueryBatchRequest.to_json())

# convert the object into a dict
query_batch_request_dict = query_batch_request_instance.to_dict()
# create an instance of QueryBatchRequest from a dict
query_batch_request_from_dict = QueryBatchRequest.from_dict(query_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


