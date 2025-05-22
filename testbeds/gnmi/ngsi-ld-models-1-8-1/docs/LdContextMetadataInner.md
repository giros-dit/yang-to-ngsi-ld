# LdContextMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**local_id** | **str** |  | 
**kind** | **str** |  | 
**timestamp** | **datetime** |  | 
**last_usage** | **datetime** |  | [optional] 
**number_of_hits** | **int** |  | [optional] 
**extra_info** | **object** |  | [optional] 

## Example

```python
from ngsi_ld_models_1_8_1.models.ld_context_metadata_inner import LdContextMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of LdContextMetadataInner from a JSON string
ld_context_metadata_inner_instance = LdContextMetadataInner.from_json(json)
# print the JSON string representation of the object
print(LdContextMetadataInner.to_json())

# convert the object into a dict
ld_context_metadata_inner_dict = ld_context_metadata_inner_instance.to_dict()
# create an instance of LdContextMetadataInner from a dict
ld_context_metadata_inner_from_dict = LdContextMetadataInner.from_dict(ld_context_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


