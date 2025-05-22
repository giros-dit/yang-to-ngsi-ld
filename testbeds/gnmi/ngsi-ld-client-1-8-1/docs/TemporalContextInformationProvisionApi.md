# ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_attrs_temporal**](TemporalContextInformationProvisionApi.md#append_attrs_temporal) | **POST** /temporal/entities/{entityId}/attrs | Temporal Representation of Entity Attribute instance addition 
[**delete_attr_instance_temporal**](TemporalContextInformationProvisionApi.md#delete_attr_instance_temporal) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | Attribute Instance deletion by instance id 
[**delete_attrs_temporal**](TemporalContextInformationProvisionApi.md#delete_attrs_temporal) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId} | Attribute from Temporal Representation of Entity deletion 
[**delete_temporal**](TemporalContextInformationProvisionApi.md#delete_temporal) | **DELETE** /temporal/entities/{entityId} | Temporal Representation of Entity deletion by id 
[**update_attrs_temporal**](TemporalContextInformationProvisionApi.md#update_attrs_temporal) | **PATCH** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | Attribute Instance update 
[**upsert_temporal**](TemporalContextInformationProvisionApi.md#upsert_temporal) | **POST** /temporal/entities | Temporal Representation of Entity creation 


# **append_attrs_temporal**
> append_attrs_temporal(entity_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity_temporal=entity_temporal)

Temporal Representation of Entity Attribute instance addition 

5.6.12 Add Attributes to Temporal Representation of an Entity.  This operation allows modifying a Temporal Representation of an Entity by adding new Attribute instances. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity_temporal import EntityTemporal
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
    api_instance = ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity_temporal = ngsi_ld_client_1_8_1.EntityTemporal() # EntityTemporal |  (optional)

    try:
        # Temporal Representation of Entity Attribute instance addition 
        api_instance.append_attrs_temporal(entity_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity_temporal=entity_temporal)
    except Exception as e:
        print("Exception when calling TemporalContextInformationProvisionApi->append_attrs_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity_temporal** | [**EntityTemporal**](EntityTemporal.md)|  | [optional] 

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
**204** | All the Attributes were added successfully.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attr_instance_temporal**
> delete_attr_instance_temporal(entity_id, attr_id, instance_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Attribute Instance deletion by instance id 

5.6.15 Delete Attribute Instance from Temporal Representation of an Entity.  This operation allows deleting one Attribute instance (Property or Relationship), identified by its instanceId, of a Temporal Representation of an Entity. The Attribute itself and all its child elements shall be deleted. This operation enables the removal of individual Attribute instances that could have been previously added to the Temporal Representation of an Entity. 

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
    api_instance = ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    instance_id = 'instance_id_example' # str | Id (URI) identifying a particular Attribute instance.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Attribute Instance deletion by instance id 
        api_instance.delete_attr_instance_temporal(entity_id, attr_id, instance_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
    except Exception as e:
        print("Exception when calling TemporalContextInformationProvisionApi->delete_attr_instance_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **instance_id** | **str**| Id (URI) identifying a particular Attribute instance. | 
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
**204** | The attribute instance was delete successfully.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attrs_temporal**
> delete_attrs_temporal(entity_id, attr_id, delete_all=delete_all, dataset_id=dataset_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Attribute from Temporal Representation of Entity deletion 

5.6.13 Delete Attributes from Temporal Representation of an Entity.  This operation allows deleting an Attribute (Property or Relationship) of the Temporal Representation of an Entity. The Attribute itself and all its children shall be deleted. 

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
    api_instance = ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    delete_all = True # bool | If true, all attribute instances are deleted. Otherwise (default) only the Attribute instance specified by the datasetId is deleted. In case neither the deleteAll flag nor a datasetId is present, the default Attribute instance is deleted.  (optional)
    dataset_id = ngsi_ld_client_1_8_1.QueryEntityDatasetIdParameter() # QueryEntityDatasetIdParameter | Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Attribute from Temporal Representation of Entity deletion 
        api_instance.delete_attrs_temporal(entity_id, attr_id, delete_all=delete_all, dataset_id=dataset_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
    except Exception as e:
        print("Exception when calling TemporalContextInformationProvisionApi->delete_attrs_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **delete_all** | **bool**| If true, all attribute instances are deleted. Otherwise (default) only the Attribute instance specified by the datasetId is deleted. In case neither the deleteAll flag nor a datasetId is present, the default Attribute instance is deleted.  | [optional] 
 **dataset_id** | [**QueryEntityDatasetIdParameter**](.md)| Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  | [optional] 
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
**204** | The attribute was deleted successfully.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_temporal**
> delete_temporal(entity_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Temporal Representation of Entity deletion by id 

5.6.16 Delete Temporal Representation of an Entity.  This operation allows deleting the Temporal Representation of an Entity. 

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
    api_instance = ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Temporal Representation of Entity deletion by id 
        api_instance.delete_temporal(entity_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
    except Exception as e:
        print("Exception when calling TemporalContextInformationProvisionApi->delete_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
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

# **update_attrs_temporal**
> update_attrs_temporal(entity_id, attr_id, instance_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity_temporal=entity_temporal)

Attribute Instance update 

5.6.14 Partial Update Attribute instance in Temporal Representation of an Entity.  This operation allows modifying a specific Attribute (Property or Relationship) instance, identified by its instanceId, of a Temporal Representation of an Entity.  This operation enables the correction of wrong information that could have been previously added to the Temporal Representation of an Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity_temporal import EntityTemporal
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
    api_instance = ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    instance_id = 'instance_id_example' # str | Id (URI) identifying a particular Attribute instance.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity_temporal = ngsi_ld_client_1_8_1.EntityTemporal() # EntityTemporal |  (optional)

    try:
        # Attribute Instance update 
        api_instance.update_attrs_temporal(entity_id, attr_id, instance_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity_temporal=entity_temporal)
    except Exception as e:
        print("Exception when calling TemporalContextInformationProvisionApi->update_attrs_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **instance_id** | **str**| Id (URI) identifying a particular Attribute instance. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity_temporal** | [**EntityTemporal**](EntityTemporal.md)|  | [optional] 

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
**204** | The attribute was updated successfully.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_temporal**
> upsert_temporal(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity_temporal=entity_temporal)

Temporal Representation of Entity creation 

5.6.11 Create or Update Temporal Representation of an Entity.  This operation allows creating or updating (by adding new Attribute instances) a Temporal Representation of an Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity_temporal import EntityTemporal
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
    api_instance = ngsi_ld_client_1_8_1.TemporalContextInformationProvisionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity_temporal = ngsi_ld_client_1_8_1.EntityTemporal() # EntityTemporal |  (optional)

    try:
        # Temporal Representation of Entity creation 
        api_instance.upsert_temporal(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity_temporal=entity_temporal)
    except Exception as e:
        print("Exception when calling TemporalContextInformationProvisionApi->upsert_temporal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity_temporal** | [**EntityTemporal**](EntityTemporal.md)|  | [optional] 

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
**201** | Upon creation success, the HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the resource URI of the created entity resource.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**204** | Upon update success.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**422** | It is used to indicate that the operation is not available, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

