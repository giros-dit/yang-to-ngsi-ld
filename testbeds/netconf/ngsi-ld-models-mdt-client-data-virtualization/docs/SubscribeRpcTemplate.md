# SubscribeRpcTemplate

NGSI-LD Entity Type that represents the template for indicating the needed parameters to trigger a SUBSCRIBE Remote Procedure Call (RPC)  operation within the server supporting a model-driven network management protocol. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SubscribeRpcTemplate. | [default to 'SubscribeRpcTemplate']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**subscription_mode** | [**SubscriptionMode**](SubscriptionMode.md) |  | 
**uses_protocol** | [**UsesProtocol**](UsesProtocol.md) |  | 

## Example

```python
from ngsi_ld_models_mdt_client_data_virtualization.models.subscribe_rpc_template import SubscribeRpcTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeRpcTemplate from a JSON string
subscribe_rpc_template_instance = SubscribeRpcTemplate.from_json(json)
# print the JSON string representation of the object
print(SubscribeRpcTemplate.to_json())

# convert the object into a dict
subscribe_rpc_template_dict = subscribe_rpc_template_instance.to_dict()
# create an instance of SubscribeRpcTemplate from a dict
subscribe_rpc_template_from_dict = SubscribeRpcTemplate.from_dict(subscribe_rpc_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


