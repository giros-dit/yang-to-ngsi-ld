# CollectorGoflow2

Within this container those data that are specific to the Goflow2 collector are included  YANG module: netflow-v9.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be CollectorGoflow2. | [default to 'CollectorGoflow2']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**time_received** | [**TimeReceived**](TimeReceived.md) |  | 
**sampler_address** | [**SamplerAddress**](SamplerAddress.md) |  | [optional] 
**sampler_address_ipv6** | [**SamplerAddressIpv6**](SamplerAddressIpv6.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.collector_goflow2 import CollectorGoflow2

# TODO update the JSON string below
json = "{}"
# create an instance of CollectorGoflow2 from a JSON string
collector_goflow2_instance = CollectorGoflow2.from_json(json)
# print the JSON string representation of the object
print CollectorGoflow2.to_json()

# convert the object into a dict
collector_goflow2_dict = collector_goflow2_instance.to_dict()
# create an instance of CollectorGoflow2 from a dict
collector_goflow2_form_dict = collector_goflow2.from_dict(collector_goflow2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

