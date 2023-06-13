# CsourceRegistrationOutputAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from ngsi_ld_models.models.csource_registration_output_all_of import CsourceRegistrationOutputAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CsourceRegistrationOutputAllOf from a JSON string
csource_registration_output_all_of_instance = CsourceRegistrationOutputAllOf.from_json(json)
# print the JSON string representation of the object
print CsourceRegistrationOutputAllOf.to_json()

# convert the object into a dict
csource_registration_output_all_of_dict = csource_registration_output_all_of_instance.to_dict()
# create an instance of CsourceRegistrationOutputAllOf from a dict
csource_registration_output_all_of_form_dict = csource_registration_output_all_of.from_dict(csource_registration_output_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


