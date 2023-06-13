# SubscriptionCommon

5.2.12 represents a Context Subscription. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription identifier (JSON-LD @id).  | [optional] 
**type** | **str** | JSON-LD @type.  | [optional] 
**subscription_name** | **str** | A (short) name given to this Subscription.  | [optional] 
**description** | **str** | Subscription description.  | [optional] 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entities subscribed.  | [optional] 
**notification_trigger** | **List[str]** | The notification triggers listed indicate what kind of changes shall trigger a notification. If not present, the default is the combination attributeCreated and attributeUpdated. entityUpdated is equivalent to the combination attributeCreated, attributeUpdated and attributeDeleted.  | [optional] [default to ["attributeCreated","attributeUpdated"]]
**q** | **str** | Query that shall be met by subscribed entities in order to trigger the notification.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) |  | [optional] 
**csf** | **str** | Context source filter that shall be met by Context Source Registrations describing Context Sources to be used for Entity Subscriptions.  | [optional] 
**is_active** | **bool** | Allows clients to temporarily pause the subscription by making it inactive. true indicates that the Subscription is under operation. false indicates that the subscription is paused and notifications shall not be delivered.  | [optional] [default to True]
**notification** | [**NotificationParams**](NotificationParams.md) |  | [optional] 
**expires_at** | **datetime** | Expiration date for the subscription.  | [optional] 
**temporal_q** | [**TemporalQuery**](TemporalQuery.md) |  | [optional] 
**scope_q** | **str** | Scope query.  | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15).  | [optional] 

## Example

```python
from ngsi_ld_models.models.subscription_common import SubscriptionCommon

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCommon from a JSON string
subscription_common_instance = SubscriptionCommon.from_json(json)
# print the JSON string representation of the object
print SubscriptionCommon.to_json()

# convert the object into a dict
subscription_common_dict = subscription_common_instance.to_dict()
# create an instance of SubscriptionCommon from a dict
subscription_common_form_dict = subscription_common.from_dict(subscription_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


