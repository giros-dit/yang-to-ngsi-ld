# PrefixSetPrefix

List of prefixes in the prefix set  YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be PrefixSetPrefix. | [default to 'PrefixSetPrefix']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ip_prefix** | [**PrefixSetPrefixIpPrefix**](PrefixSetPrefixIpPrefix.md) |  | [optional] 
**mask_length_range** | [**MaskLengthRange**](MaskLengthRange.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.prefix_set_prefix import PrefixSetPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of PrefixSetPrefix from a JSON string
prefix_set_prefix_instance = PrefixSetPrefix.from_json(json)
# print the JSON string representation of the object
print(PrefixSetPrefix.to_json())

# convert the object into a dict
prefix_set_prefix_dict = prefix_set_prefix_instance.to_dict()
# create an instance of PrefixSetPrefix from a dict
prefix_set_prefix_from_dict = PrefixSetPrefix.from_dict(prefix_set_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


