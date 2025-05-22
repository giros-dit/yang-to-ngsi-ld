# ngsi_ld_client_1_8_1.ContextSourceIdentityInformationOperationsApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_cs_identity_info**](ContextSourceIdentityInformationOperationsApi.md#retrieve_cs_identity_info) | **GET** /info/sourceIdentity | Context Source Identity Retrieval  


# **retrieve_cs_identity_info**
> ContextSourceIdentity retrieve_cs_identity_info(link=link, ngsild_tenant=ngsild_tenant)

Context Source Identity Retrieval  

5.15.1 Retrieve Context Source Identity Information.  With this operation, a client can obtain Context Source identity information which uniquely defines the Context Source itself.  In the multi-tenancy use case (see clause 4.14), a client can obtain identify information about a specific Tenant within a Context Source. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.context_source_identity import ContextSourceIdentity
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
    api_instance = ngsi_ld_client_1_8_1.ContextSourceIdentityInformationOperationsApi(api_client)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Context Source Identity Retrieval  
        api_response = api_instance.retrieve_cs_identity_info(link=link, ngsild_tenant=ngsild_tenant)
        print("The response of ContextSourceIdentityInformationOperationsApi->retrieve_cs_identity_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextSourceIdentityInformationOperationsApi->retrieve_cs_identity_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**ContextSourceIdentity**](ContextSourceIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the Context Source Identity Information.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**501** | It is used by Registered Context Sources to indicate that the data format  of the request is unsupported see clause 6.3.7.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

