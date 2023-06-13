# UpdateCSRRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique registration identifier. (JSON-LD @id). There may be multiple registrations per Context Source, i.e. the id is unique per registration.  | [optional] 
**type** | **str** | JSON-LD @type Use reserved type for identifying Context Source Registration.  | [optional] 
**registration_name** | **str** | A name given to this Context Source Registration.  | [optional] 
**description** | **str** | A description of this Context Source Registration.  | [optional] 
**information** | [**List[RegistrationInfo]**](RegistrationInfo.md) | Describes the Entities, Properties and Relationships for which the Context Source may be able to provide information.  | [optional] 
**tenant** | **str** | Identifies the tenant that has to be specified in all requests to the Context Source that are related to the information registered in this Context Source Registration. If not present, the default tenant is assumed. Should only be present in systems supporting multi-tenancy.  | [optional] 
**observation_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**management_interval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**location** | [**Geometry**](Geometry.md) |  | [optional] 
**observation_space** | [**Geometry**](Geometry.md) |  | [optional] 
**operation_space** | [**Geometry**](Geometry.md) |  | [optional] 
**expires_at** | **datetime** | Provides an expiration date. When passed the Context Source Registration will become invalid and the Context Source might no longer be available.  | [optional] 
**endpoint** | **str** | Endpoint expressed as dereferenceable URI through which the Context Source exposes its NGSI-LD interface.  | [optional] 
**context_source_info** | [**List[KeyValuePair]**](KeyValuePair.md) | Generic {key, value} array to convey optional information to provide when contacting the registered Context Source.  | [optional] 
**scope** | [**CsourceRegistrationFragmentScope**](CsourceRegistrationFragmentScope.md) |  | [optional] 
**mode** | **str** | The definition of the mode of distributed operation (see clause 4.3.6) supported by the registered Context Source.  | [optional] [default to 'inclusive']
**operations** | **List[str]** | The definition limited subset of API operations supported by the registered Context Source.  If undefined, the default set of operations is \&quot;federationOps\&quot; (see clause 4.20).  | [optional] 
**refresh_rate** | **str** | An indication of the likely period of time to elapse between updates at this registered endpoint. Brokers may optionally use this information to help implement caching.  | [optional] 
**management** | [**RegistrationManagementInfo**](RegistrationManagementInfo.md) |  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.update_csr_request import UpdateCSRRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCSRRequest from a JSON string
update_csr_request_instance = UpdateCSRRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCSRRequest.to_json()

# convert the object into a dict
update_csr_request_dict = update_csr_request_instance.to_dict()
# create an instance of UpdateCSRRequest from a dict
update_csr_request_form_dict = update_csr_request.from_dict(update_csr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


