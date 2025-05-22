# ngsi_ld_client_1_8_1.JSONLDContextAPIApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_context**](JSONLDContextAPIApi.md#create_context) | **POST** /jsonldContexts | Add a user @context to the internal cache 
[**delete_context**](JSONLDContextAPIApi.md#delete_context) | **DELETE** /jsonldContexts/{contextId} | Delete one specific @context from internal cache, possibly re-inserting a freshly downloaded copy of it 
[**list_contexts**](JSONLDContextAPIApi.md#list_contexts) | **GET** /jsonldContexts | List all cached @contexts 
[**retrieve_context**](JSONLDContextAPIApi.md#retrieve_context) | **GET** /jsonldContexts/{contextId} | Serve one specific user @context 


# **create_context**
> create_context(ngsild_tenant=ngsild_tenant, create_context_request=create_context_request)

Add a user @context to the internal cache 

5.13.2 Add @context.  With this operation, a client can ask the Broker to store the full content of a specific @context, by giving it to the Broker. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.create_context_request import CreateContextRequest
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
    api_instance = ngsi_ld_client_1_8_1.JSONLDContextAPIApi(api_client)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    create_context_request = ngsi_ld_client_1_8_1.CreateContextRequest() # CreateContextRequest | Payload body in the request contains a JSON object that has a root node named @context, which represents a JSON-LD \"local\" context.  (optional)

    try:
        # Add a user @context to the internal cache 
        api_instance.create_context(ngsild_tenant=ngsild_tenant, create_context_request=create_context_request)
    except Exception as e:
        print("Exception when calling JSONLDContextAPIApi->create_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **create_context_request** | [**CreateContextRequest**](CreateContextRequest.md)| Payload body in the request contains a JSON object that has a root node named @context, which represents a JSON-LD \&quot;local\&quot; context.  | [optional] 

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
**201** | The HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the local URI of the added @context.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_context**
> delete_context(context_id, reload=reload, ngsild_tenant=ngsild_tenant)

Delete one specific @context from internal cache, possibly re-inserting a freshly downloaded copy of it 

5.13.5 Delete and Reload @context  With this operation, a client supplies a local identifier to the Broker, indicating a stored @context, that the Broker shall remove from its storage. For @contexts of kind \"Cached\" this can also be the original URL the Broker downloaded the @context from. If the entry in the local storage that corresponds to the identifier is itself an array of @contexts, this operation will not delete the children, i.e. the @contexts in the array, but just the entry. 

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
    api_instance = ngsi_ld_client_1_8_1.JSONLDContextAPIApi(api_client)
    context_id = 'context_id_example' # str | Local identifier of the @context to be managed (served or deleted). For @contexts of kind \"Cached\" this can also be the original URL the Broker downloaded the @context from. 
    reload = True # bool | Indicates to perform a download and replace of the @context, as specified in clause 5.13.5.4.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Delete one specific @context from internal cache, possibly re-inserting a freshly downloaded copy of it 
        api_instance.delete_context(context_id, reload=reload, ngsild_tenant=ngsild_tenant)
    except Exception as e:
        print("Exception when calling JSONLDContextAPIApi->delete_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Local identifier of the @context to be managed (served or deleted). For @contexts of kind \&quot;Cached\&quot; this can also be the original URL the Broker downloaded the @context from.  | 
 **reload** | **bool**| Indicates to perform a download and replace of the @context, as specified in clause 5.13.5.4.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

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
**504** | It is used when re-downloading fails.  |  * NGSILD-Tenant -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contexts**
> ListContexts200Response list_contexts(details=details, kind=kind, ngsild_tenant=ngsild_tenant)

List all cached @contexts 

5.13.3 List @contexts.  With this operation a client can obtain a list of URLs that represent all of the @contexts stored in the local context store of the Broker. Each URL can be used to download the corresponding @context, and, in case the @context's kind is \"Cached\", it shall be the original URL the Broker downloaded the @context from.  In case a \"details\" flag is set to true, the client obtains a list of JSON objects, each representing information (metadata) about an @context currently stored by the Broker. Each JSON object contains information about the @context's original URL (if any), its local identifier in the Broker's storage, its kind (\"Cached\", \"Hosted\" and \"ImplicitlyCreated\"), its creation timestamp, its expiry date (if \"Cached\"), and additional optional information. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.list_contexts200_response import ListContexts200Response
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
    api_instance = ngsi_ld_client_1_8_1.JSONLDContextAPIApi(api_client)
    details = True # bool | Whether a list of URLs or a more detailed list of JSON Objects is requested. (optional)
    kind = 'kind_example' # str | Can be either \"Cached\", \"Hosted\", or \"ImplicitlyCreated\".  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # List all cached @contexts 
        api_response = api_instance.list_contexts(details=details, kind=kind, ngsild_tenant=ngsild_tenant)
        print("The response of JSONLDContextAPIApi->list_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JSONLDContextAPIApi->list_contexts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **bool**| Whether a list of URLs or a more detailed list of JSON Objects is requested. | [optional] 
 **kind** | **str**| Can be either \&quot;Cached\&quot;, \&quot;Hosted\&quot;, or \&quot;ImplicitlyCreated\&quot;.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**ListContexts200Response**](ListContexts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing a list of URLs or a list of JSON Objects, as defined in clause 5.13.3.5, representing metadata about stored @contexts.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_context**
> RetrieveContext200Response retrieve_context(context_id, details=details, ngsild_tenant=ngsild_tenant)

Serve one specific user @context 

5.13.4 Serve @context.  With this operation a client can obtain the full content of a specific @context (only for @contexts of kind \"Hosted\" or \"ImplicitlyCreated\"), which is currently stored in the Broker's internal storage, or its metadata (for all kinds of stored @contexts). 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.retrieve_context200_response import RetrieveContext200Response
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
    api_instance = ngsi_ld_client_1_8_1.JSONLDContextAPIApi(api_client)
    context_id = 'context_id_example' # str | Local identifier of the @context to be managed (served or deleted). For @contexts of kind \"Cached\" this can also be the original URL the Broker downloaded the @context from. 
    details = True # bool | Whether a list of URLs or a more detailed list of JSON Objects is requested. (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Serve one specific user @context 
        api_response = api_instance.retrieve_context(context_id, details=details, ngsild_tenant=ngsild_tenant)
        print("The response of JSONLDContextAPIApi->retrieve_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JSONLDContextAPIApi->retrieve_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Local identifier of the @context to be managed (served or deleted). For @contexts of kind \&quot;Cached\&quot; this can also be the original URL the Broker downloaded the @context from.  | 
 **details** | **bool**| Whether a list of URLs or a more detailed list of JSON Objects is requested. | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**RetrieveContext200Response**](RetrieveContext200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the parameter details is False or missing, response body contains a JSON object that has a root node named @context, which represents a JSON-LD \&quot;local context\&quot;. If the parameter details is True, response body contains a JSON object as defined in clause 5.13.4.5, which metadata of a JSON-LD \&quot;local context\&quot;.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**422** | It is used to indicate that the operation is not available, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

