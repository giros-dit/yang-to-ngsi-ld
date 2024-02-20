# QuerySubscription200ResponseInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription identifier (JSON-LD @id).  | 
**type** | **str** | JSON-LD @type.  | 
**subscription_name** | **str** | A (short) name given to this Subscription.  | [optional] 
**description** | **str** | Subscription description.  | [optional] 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entities subscribed.  | 
**notification_trigger** | **List[str]** | The notification triggers listed indicate what kind of changes shall trigger a notification. If not present, the default is the combination attributeCreated and attributeUpdated. entityUpdated is equivalent to the combination attributeCreated, attributeUpdated and attributeDeleted.  | [optional] 
**q** | **str** | Query that shall be met by subscribed entities in order to trigger the notification.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) |  | [optional] 
**csf** | **str** | Context source filter that shall be met by Context Source Registrations describing Context Sources to be used for Entity Subscriptions.  | [optional] 
**is_active** | **bool** | Allows clients to temporarily pause the subscription by making it inactive. true indicates that the Subscription is under operation. false indicates that the subscription is paused and notifications shall not be delivered.  | [optional] 
**notification** | [**NotificationParams**](NotificationParams.md) |  | 
**expires_at** | **datetime** | Expiration date for the subscription.  | [optional] 
**temporal_q** | [**TemporalQuery**](TemporalQuery.md) |  | [optional] 
**scope_q** | **str** | Scope query.  | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15).  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**status** | **str** | Read-only. Provided by the system when querying the details of a subscription.  | [optional] [readonly] 
**watched_attributes** | **List[str]** | Watched Attributes (Properties or Relationships). If not defined it means any Attribute.  | [optional] 
**throttling** | **float** | Minimal period of time in seconds which shall elapse between two consecutive notifications.  | [optional] 
**time_interval** | **float** | Indicates that a notification shall be delivered periodically regardless of attribute changes. Actually, when the time interval (in seconds) specified in this value field is reached.  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.query_subscription200_response_inner1 import QuerySubscription200ResponseInner1

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySubscription200ResponseInner1 from a JSON string
query_subscription200_response_inner1_instance = QuerySubscription200ResponseInner1.from_json(json)
# print the JSON string representation of the object
print QuerySubscription200ResponseInner1.to_json()

# convert the object into a dict
query_subscription200_response_inner1_dict = query_subscription200_response_inner1_instance.to_dict()
# create an instance of QuerySubscription200ResponseInner1 from a dict
query_subscription200_response_inner1_form_dict = query_subscription200_response_inner1.from_dict(query_subscription200_response_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


