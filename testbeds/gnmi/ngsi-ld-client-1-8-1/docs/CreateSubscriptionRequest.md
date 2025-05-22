# CreateSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription identifier (JSON-LD @id).  | [optional] 
**type** | **str** | JSON-LD @type.  | 
**subscription_name** | **str** | A (short) name given to this Subscription.  | [optional] 
**description** | **str** | Subscription description.  | [optional] 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entities subscribed.  Mandatory if timeInterval is present, unless the execution of the request  is limited to local scope (see clause 5.5.13).  | [optional] 
**local_only** | **bool** | If localOnly&#x3D;true then the subscription only pertains to the Entities  stored locally (see clause 5.5.13).  | [optional] 
**notification_trigger** | **List[str]** | The notification triggers listed indicate what kind of changes shall trigger a notification. If not present, the default is the combination attributeCreated and attributeUpdated. entityUpdated is equivalent to the combination attributeCreated, attributeUpdated and attributeDeleted.  | [optional] 
**q** | **str** | Query that shall be met by subscribed entities in order to trigger the notification.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) |  | [optional] 
**csf** | **str** | Context source filter that shall be met by Context Source Registrations describing Context Sources to be used for Entity Subscriptions.  | [optional] 
**is_active** | **bool** | Allows clients to temporarily pause the subscription by making it inactive. true indicates that the Subscription is under operation. false indicates that the subscription is paused and notifications shall not be delivered.  | [optional] [default to True]
**notification** | [**NotificationParams**](NotificationParams.md) |  | 
**expires_at** | **datetime** | Expiration date for the subscription.  | [optional] 
**temporal_q** | [**TemporalQuery**](TemporalQuery.md) |  | [optional] 
**scope_q** | **str** | Scope query.  | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15).  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**status** | **str** | Read-only. Provided by the system when querying the details of a subscription.  | [optional] [readonly] 
**jsonld_context** | **str** | The dereferenceable URI of the JSON-LD @context to be used when sending  a notification resulting from the subscription. If not provided, the @context used for the subscription shall be used as a default.  | [optional] 
**dataset_id** | **List[str]** | Specifies the datasetIds of the Attribute instances to be selected for each  matched Attribute as per clause 4.5.5. Valid URIs, \&quot;@none\&quot; for including the  default Attribute instances.  | [optional] 
**watched_attributes** | **List[str]** | Watched Attributes (Properties or Relationships). If not defined it means any Attribute.  | [optional] 
**throttling** | **float** | Minimal period of time in seconds which shall elapse between two consecutive notifications.  | [optional] 
**time_interval** | **float** | Indicates that a notification shall be delivered periodically regardless of attribute changes. Actually, when the time interval (in seconds) specified in this value field is reached.  | [optional] 

## Example

```python
from ngsi_ld_client_1_8_1.models.create_subscription_request import CreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequest from a JSON string
create_subscription_request_instance = CreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionRequest.to_json())

# convert the object into a dict
create_subscription_request_dict = create_subscription_request_instance.to_dict()
# create an instance of CreateSubscriptionRequest from a dict
create_subscription_request_from_dict = CreateSubscriptionRequest.from_dict(create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


