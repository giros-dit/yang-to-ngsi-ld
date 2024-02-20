# RegistrationManagementInfo

5.2.34 This type represents the data to alter the default behaviour of a Context Broker when making a distributed operation request to a registered Context Source. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_only** | **bool** | If localOnly&#x3D;true then distributed operations associated to this Context Source Registration will act only on data held directly by the registered Context Source itself (see clause 4.3.6.4).  | [optional] 
**cache_duration** | **str** | Minimal period of time which shall elapse between two consecutive context information consumption operations (as defined in clause 5.7) related to the same context data will occur. If the cacheDuration latency period has not been reached, a cached value for the entity or its attributes shall be returned where available.  | [optional] 
**timeout** | **float** | Maximum period of time in milliseconds which may elapse before a forwarded request is assumed to have failed.  | [optional] 
**cooldown** | **float** | Minimum period of time in milliseconds which shall elapse before attempting to make a subsequent forwarded request to the same endpoint after failure. If requests are received before the cooldown period has expired, a timeout error response for the registration is automatically returned.  | [optional] 

## Example

```python
from ngsi_ld_models.models.registration_management_info import RegistrationManagementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationManagementInfo from a JSON string
registration_management_info_instance = RegistrationManagementInfo.from_json(json)
# print the JSON string representation of the object
print RegistrationManagementInfo.to_json()

# convert the object into a dict
registration_management_info_dict = registration_management_info_instance.to_dict()
# create an instance of RegistrationManagementInfo from a dict
registration_management_info_form_dict = registration_management_info.from_dict(registration_management_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


