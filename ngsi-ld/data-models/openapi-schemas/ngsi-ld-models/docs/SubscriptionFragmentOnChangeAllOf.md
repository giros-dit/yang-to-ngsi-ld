# SubscriptionFragmentOnChangeAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watched_attributes** | **List[str]** | Watched Attributes (Properties or Relationships). If not defined it means any Attribute.  | [optional] 
**throttling** | **float** | Minimal period of time in seconds which shall elapse between two consecutive notifications.  | [optional] 

## Example

```python
from ngsi_ld_models.models.subscription_fragment_on_change_all_of import SubscriptionFragmentOnChangeAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionFragmentOnChangeAllOf from a JSON string
subscription_fragment_on_change_all_of_instance = SubscriptionFragmentOnChangeAllOf.from_json(json)
# print the JSON string representation of the object
print SubscriptionFragmentOnChangeAllOf.to_json()

# convert the object into a dict
subscription_fragment_on_change_all_of_dict = subscription_fragment_on_change_all_of_instance.to_dict()
# create an instance of SubscriptionFragmentOnChangeAllOf from a dict
subscription_fragment_on_change_all_of_form_dict = subscription_fragment_on_change_all_of.from_dict(subscription_fragment_on_change_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


