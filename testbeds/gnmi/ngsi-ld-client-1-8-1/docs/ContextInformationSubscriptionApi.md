# ngsi_ld_client_1_8_1.ContextInformationSubscriptionApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](ContextInformationSubscriptionApi.md#create_subscription) | **POST** /subscriptions | Create Subscription 
[**delete_subscription**](ContextInformationSubscriptionApi.md#delete_subscription) | **DELETE** /subscriptions/{subscriptionId} | Subscription deletion by id 
[**query_subscription**](ContextInformationSubscriptionApi.md#query_subscription) | **GET** /subscriptions | Retrieve list of Subscriptions 
[**retrieve_subscription**](ContextInformationSubscriptionApi.md#retrieve_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription retrieval by id 
[**update_subscription**](ContextInformationSubscriptionApi.md#update_subscription) | **PATCH** /subscriptions/{subscriptionId} | Subscription update by id 


# **create_subscription**
> create_subscription(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, create_subscription_request=create_subscription_request)

Create Subscription 

5.8.1 Create subscription.  This operation allows creating a new subscription. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationSubscriptionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    create_subscription_request = ngsi_ld_client_1_8_1.CreateSubscriptionRequest() # CreateSubscriptionRequest |  (optional)

    try:
        # Create Subscription 
        api_instance.create_subscription(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, create_subscription_request=create_subscription_request)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **create_subscription_request** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the resource URI of the created subscription resource.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**409** | It is used to indicate that the entity or an exclusive or redirect registration defining the entity already exists, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Subscription deletion by id 

5.8.5 Delete Subscription.  This operation allows deleting an existing subscription. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Subscription deletion by id 
        api_instance.delete_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_subscription**
> List[QuerySubscription200ResponseInner] query_subscription(options=options, limit=limit, count=count, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Retrieve list of Subscriptions 

5.8.4 Query Subscriptions.  This operation allows querying existing Subscriptions. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client_1_8_1.models.query_subscription200_response_inner import QuerySubscription200ResponseInner
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationSubscriptionApi(api_client)
    options = [ngsi_ld_client_1_8_1.OptionsSysAttrs()] # List[OptionsSysAttrs] |  (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    count = True # bool | 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \"limit\" URI parameter), the total number of matching results (e.g. number of Entities) is returned.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Retrieve list of Subscriptions 
        api_response = api_instance.query_subscription(options=options, limit=limit, count=count, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationSubscriptionApi->query_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->query_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**List[OptionsSysAttrs]**](OptionsSysAttrs.md)|  | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **count** | **bool**| 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \&quot;limit\&quot; URI parameter), the total number of matching results (e.g. number of Entities) is returned.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**List[QuerySubscription200ResponseInner]**](QuerySubscription200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing a list of subscriptions.  |  * NGSILD-Tenant -  <br>  * NGSILD-Results-Count -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_subscription**
> QuerySubscription200ResponseInner retrieve_subscription(subscription_id, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Subscription retrieval by id 

5.8.3 Retrieve Subscription.  This operation allows retrieving an existing subscription. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client_1_8_1.models.query_subscription200_response_inner import QuerySubscription200ResponseInner
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    options = [ngsi_ld_client_1_8_1.OptionsSysAttrs()] # List[OptionsSysAttrs] |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Subscription retrieval by id 
        api_response = api_instance.retrieve_subscription(subscription_id, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationSubscriptionApi->retrieve_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->retrieve_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **options** | [**List[OptionsSysAttrs]**](OptionsSysAttrs.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**QuerySubscription200ResponseInner**](QuerySubscription200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the target subscription.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> update_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, subscription=subscription)

Subscription update by id 

5.8.2 Update Subscription.  This operation allows updating an existing subscription. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.subscription import Subscription
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationSubscriptionApi(api_client)
    subscription_id = 'subscription_id_example' # str | Id (URI) of the concerned subscription.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    subscription = ngsi_ld_client_1_8_1.Subscription() # Subscription |  (optional)

    try:
        # Subscription update by id 
        api_instance.update_subscription(subscription_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, subscription=subscription)
    except Exception as e:
        print("Exception when calling ContextInformationSubscriptionApi->update_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id (URI) of the concerned subscription. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

