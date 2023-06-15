# RetrieveCSR200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**id** | **str** | Unique registration identifier. (JSON-LD @id). There may be multiple registrations per Context Source, i.e. the id is unique per registration.  | 
**type** | **str** | JSON-LD @type Use reserved type for identifying Context Source Registration.  | 
**registration_name** | **str** | A name given to this Context Source Registration.  | [optional] 
**description** | **str** | A description of this Context Source Registration.  | [optional] 
**information** | [**List[RegistrationInfo]**](RegistrationInfo.md) | Describes the Entities, Properties and Relationships for which the Context Source may be able to provide information.  | 
**tenant** | **str** | Identifies the tenant that has to be specified in all requests to the Context Source that are related to the information registered in this Context Source Registration. If not present, the default tenant is assumed. Should only be present in systems supporting multi-tenancy.  | [optional] 
**observation_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**management_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**location** | [**Geometry**](Geometry.md) |  | [optional] 
**observation_space** | [**Geometry**](Geometry.md) |  | [optional] 
**operation_space** | [**Geometry**](Geometry.md) |  | [optional] 
**expires_at** | **datetime** | Provides an expiration date. When passed the Context Source Registration will become invalid and the Context Source might no longer be available.  | [optional] 
**endpoint** | **str** | Endpoint expressed as dereferenceable URI through which the Context Source exposes its NGSI-LD interface.  | 
**context_source_info** | [**List[KeyValuePair]**](KeyValuePair.md) | Generic {key, value} array to convey optional information to provide when contacting the registered Context Source.  | [optional] 
**scope** | [**CsourceRegistrationFragmentScope**](CsourceRegistrationFragmentScope.md) |  | [optional] 
**mode** | **str** | The definition of the mode of distributed operation (see clause 4.3.6) supported by the registered Context Source.  | [optional] [default to 'inclusive']
**operations** | **List[str]** | The definition limited subset of API operations supported by the registered Context Source.  If undefined, the default set of operations is \&quot;federationOps\&quot; (see clause 4.20).  | [optional] 
**refresh_rate** | **str** | An indication of the likely period of time to elapse between updates at this registered endpoint. Brokers may optionally use this information to help implement caching.  | [optional] 
**management** | [**RegistrationManagementInfo**](RegistrationManagementInfo.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**status** | **str** | Read-only. Status of the Registration. It shall be \&quot;ok\&quot; if the last attempt to perform a distributed operation succeeded. It shall be \&quot;failed\&quot; if the last attempt to perform a distributed operation failed.  | [optional] 
**times_sent** | **float** | Number of times that the registration triggered a distributed operation, including failed attempts.  | [optional] 
**times_failed** | **float** | Number of times that the registration triggered a distributed operation request that failed. | [optional] 
**last_success** | **datetime** | Timestamp corresponding to the instant when the last successfully distributed operation was sent. Created on first successful operation.  | [optional] 
**last_failure** | **datetime** | Timestamp corresponding to the instant when the last distributed operation resulting in a failure (for instance, in the HTTP binding, an HTTP response code other than 2xx) was returned.  | [optional] 

## Example

```python
from ngsi_ld_models.models.retrieve_csr200_response import RetrieveCSR200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveCSR200Response from a JSON string
retrieve_csr200_response_instance = RetrieveCSR200Response.from_json(json)
# print the JSON string representation of the object
print RetrieveCSR200Response.to_json()

# convert the object into a dict
retrieve_csr200_response_dict = retrieve_csr200_response_instance.to_dict()
# create an instance of RetrieveCSR200Response from a dict
retrieve_csr200_response_form_dict = retrieve_csr200_response.from_dict(retrieve_csr200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


