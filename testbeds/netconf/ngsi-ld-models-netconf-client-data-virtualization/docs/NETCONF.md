# NETCONF

NGSI-LD Entity Type that represents a NETCONF client. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NETCONF. | [default to 'NETCONF']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**host** | [**Host**](Host.md) |  | 
**port** | [**Port**](Port.md) |  | 
**username** | [**Username**](Username.md) |  | 
**password** | [**Password**](Password.md) |  | 
**host_family** | [**HostFamily**](HostFamily.md) |  | 
**host_key_verify** | [**HostKeyVerify**](HostKeyVerify.md) |  | [optional] 
**subscription_mode** | [**SubscriptionMode**](SubscriptionMode.md) |  | [optional] 
**xpath** | [**Xpath**](Xpath.md) |  | 

## Example

```python
from ngsi_ld_models_netconf_client_data_virtualization.models.netconf import NETCONF

# TODO update the JSON string below
json = "{}"
# create an instance of NETCONF from a JSON string
netconf_instance = NETCONF.from_json(json)
# print the JSON string representation of the object
print(NETCONF.to_json())

# convert the object into a dict
netconf_dict = netconf_instance.to_dict()
# create an instance of NETCONF from a dict
netconf_from_dict = NETCONF.from_dict(netconf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


