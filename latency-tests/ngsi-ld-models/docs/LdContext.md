# LdContext

5.2.3 JSON-LD @context  When encoding NGSI-LD Entities, Context Source Registrations, Subscriptions and Notifications, as pure JSON-LD (MIME type \"application/ld+json\"), a proper @context shall be included as a special member of the corresponding JSON-LD Object. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models.models.ld_context import LdContext

# TODO update the JSON string below
json = "{}"
# create an instance of LdContext from a JSON string
ld_context_instance = LdContext.from_json(json)
# print the JSON string representation of the object
print LdContext.to_json()

# convert the object into a dict
ld_context_dict = ld_context_instance.to_dict()
# create an instance of LdContext from a dict
ld_context_form_dict = ld_context.from_dict(ld_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


