# Tunnel

The name that identifies the remote system of the tunnel  YANG module: srl_nokia-pw-tunnel.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be Tunnel. | [default to 'Tunnel']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**TunnelName**](TunnelName.md) |  | 
**remote_system** | [**RemoteSystem**](RemoteSystem.md) |  | 
**index** | [**TunnelIndex**](TunnelIndex.md) |  | [optional] 
**allowed_tunnel_types** | [**TunnelAllowedTunnelTypes**](TunnelAllowedTunnelTypes.md) |  | [optional] 
**last_change** | [**TunnelLastChange**](TunnelLastChange.md) |  | [optional] 
**operational_tunnel_type** | [**OperationalTunnelType**](OperationalTunnelType.md) |  | [optional] 
**operational_tunnel_id** | [**OperationalTunnelId**](OperationalTunnelId.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.tunnel import Tunnel

# TODO update the JSON string below
json = "{}"
# create an instance of Tunnel from a JSON string
tunnel_instance = Tunnel.from_json(json)
# print the JSON string representation of the object
print(Tunnel.to_json())

# convert the object into a dict
tunnel_dict = tunnel_instance.to_dict()
# create an instance of Tunnel from a dict
tunnel_from_dict = Tunnel.from_dict(tunnel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


