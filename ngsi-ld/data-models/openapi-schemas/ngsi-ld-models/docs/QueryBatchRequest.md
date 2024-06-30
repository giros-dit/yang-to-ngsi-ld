# QueryBatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | JSON-LD @type.  | 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved.  | [optional] 
**attrs** | **List[str]** | List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved.  | [optional] 
**q** | **str** | Query that shall be matched by Entities in order to be retrieved.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) |  | [optional] 
**csf** | **str** | Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities.  | [optional] 
**temporal_q** | [**TemporalQuery**](TemporalQuery.md) |  | [optional] 
**scope_q** | **str** | Scope query. | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15). | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.query_batch_request import QueryBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBatchRequest from a JSON string
query_batch_request_instance = QueryBatchRequest.from_json(json)
# print the JSON string representation of the object
print QueryBatchRequest.to_json()

# convert the object into a dict
query_batch_request_dict = query_batch_request_instance.to_dict()
# create an instance of QueryBatchRequest from a dict
query_batch_request_form_dict = query_batch_request.from_dict(query_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


