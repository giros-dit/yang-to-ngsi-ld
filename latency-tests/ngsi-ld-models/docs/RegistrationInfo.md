# RegistrationInfo

5.2.10 RegistrationInfo. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[EntityInfo]**](EntityInfo.md) | Describes the entities for which the CSource may be able to provide information.  | [optional] 
**property_names** | **List[str]** | Describes the Properties that the CSource may be able to provide.  | [optional] 
**relationship_names** | **List[str]** | Describes the Relationships that the CSource may be able to provide.  | [optional] 

## Example

```python
from ngsi_ld_models.models.registration_info import RegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInfo from a JSON string
registration_info_instance = RegistrationInfo.from_json(json)
# print the JSON string representation of the object
print RegistrationInfo.to_json()

# convert the object into a dict
registration_info_dict = registration_info_instance.to_dict()
# create an instance of RegistrationInfo from a dict
registration_info_form_dict = registration_info.from_dict(registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


