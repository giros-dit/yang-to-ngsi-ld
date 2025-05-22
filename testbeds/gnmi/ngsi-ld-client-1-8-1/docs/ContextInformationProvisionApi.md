# ngsi_ld_client_1_8_1.ContextInformationProvisionApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_attrs**](ContextInformationProvisionApi.md#append_attrs) | **POST** /entities/{entityId}/attrs | Append Attributes to Entity 
[**create_batch**](ContextInformationProvisionApi.md#create_batch) | **POST** /entityOperations/create | Batch Entity Creation 
[**create_entity**](ContextInformationProvisionApi.md#create_entity) | **POST** /entities | Entity creation 
[**delete_attrs**](ContextInformationProvisionApi.md#delete_attrs) | **DELETE** /entities/{entityId}/attrs/{attrId} | Attribute delete 
[**delete_batch**](ContextInformationProvisionApi.md#delete_batch) | **POST** /entityOperations/delete | Batch Entity Delete 
[**delete_entity**](ContextInformationProvisionApi.md#delete_entity) | **DELETE** /entities/{entityId} | Entity deletion by id 
[**merge_batch**](ContextInformationProvisionApi.md#merge_batch) | **POST** /entityOperations/merge | Batch Entity Merge 
[**merge_entity**](ContextInformationProvisionApi.md#merge_entity) | **PATCH** /entities/{entityId} | Entity merge by id 
[**replace_attrs**](ContextInformationProvisionApi.md#replace_attrs) | **PUT** /entities/{entityId}/attrs/{attrId} | Attribute replace 
[**replace_entity**](ContextInformationProvisionApi.md#replace_entity) | **PUT** /entities/{entityId} | Entity replacement by id 
[**update_attrs**](ContextInformationProvisionApi.md#update_attrs) | **PATCH** /entities/{entityId}/attrs/{attrId} | Partial Attribute Update 
[**update_batch**](ContextInformationProvisionApi.md#update_batch) | **POST** /entityOperations/update | Batch Entity Update 
[**update_entity**](ContextInformationProvisionApi.md#update_entity) | **PATCH** /entities/{entityId}/attrs | Update Attributes of an Entity 
[**upsert_batch**](ContextInformationProvisionApi.md#upsert_batch) | **POST** /entityOperations/upsert | Batch Entity Creation or Update (Upsert) 


# **append_attrs**
> append_attrs(entity_id, type=type, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)

Append Attributes to Entity 

5.6.3 Append Entity Attributes.  This operation allows modifying an NGSI-LD Entity by adding new attributes (Properties or Relationships). 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity import Entity
from ngsi_ld_client_1_8_1.models.options_no_overwrite import OptionsNoOverwrite
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    options = [ngsi_ld_client_1_8_1.OptionsNoOverwrite()] # List[OptionsNoOverwrite] |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity = ngsi_ld_client_1_8_1.Entity() # Entity | Entity Fragment containing a complete representation of the Attributes to be added.  (optional)

    try:
        # Append Attributes to Entity 
        api_instance.append_attrs(entity_id, type=type, options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->append_attrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **options** | [**List[OptionsNoOverwrite]**](OptionsNoOverwrite.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity** | [**Entity**](Entity.md)| Entity Fragment containing a complete representation of the Attributes to be added.  | [optional] 

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
**204** | All the Attributes were appended successfully.  |  * NGSILD-Tenant -  <br>  |
**207** | Only the Attributes included in the response payload body were successfully appended. If no Attributes were successfully updated the updated array of UpdateResult (see clause 5.2.18) will be empty.  If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation.  In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a UpdateResult structure.  Names of the Attributes included in the UpdateResult structure are represented as Fully Qualified Names as per clause 6.3.6.  Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch**
> List[str] create_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)

Batch Entity Creation 

5.6.7 Batch Entity Creation.  This operation allows creating a batch of NGSI-LD Entities. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    query_entity200_response_inner = [ngsi_ld_client_1_8_1.QueryEntity200ResponseInner()] # List[QueryEntity200ResponseInner] | Array of entities to be created.  (optional)

    try:
        # Batch Entity Creation 
        api_response = api_instance.create_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)
        print("The response of ContextInformationProvisionApi->create_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->create_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **query_entity200_response_inner** | [**List[QueryEntity200ResponseInner]**](QueryEntity200ResponseInner.md)| Array of entities to be created.  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | If all entities have been successfully created, an array of Strings containing URIs is returned in the response. Each URI represents the Entity Id of a created entity. There is no restriction as to the order of the Entity Ids.  |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> create_entity(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)

Entity creation 

5.6.1 Create Entity  This operation allows creating a new NGSI-LD Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    query_entity200_response_inner = ngsi_ld_client_1_8_1.QueryEntity200ResponseInner() # QueryEntity200ResponseInner | Payload body in the request contains a JSON-LD object which represents the entity that is to be created.  (optional)

    try:
        # Entity creation 
        api_instance.create_entity(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **query_entity200_response_inner** | [**QueryEntity200ResponseInner**](QueryEntity200ResponseInner.md)| Payload body in the request contains a JSON-LD object which represents the entity that is to be created.  | [optional] 

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
**201** | The HTTP response shall include a \&quot;Location\&quot; HTTP header that contains the resource URI of the created entity resource.  |  * Location -  <br>  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**409** | It is used to indicate that the entity or an exclusive or redirect registration defining the entity already exists, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  |
**422** | It is used to indicate that the operation is not available, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attrs**
> delete_attrs(entity_id, attr_id, delete_all=delete_all, dataset_id=dataset_id, type=type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Attribute delete 

5.6.5 Delete Entity Attribute.  This operation allows deleting an NGSI-LD Entity's Attribute (Property or Relationship).  The Attribute itself and all its children shall be deleted. 

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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    delete_all = True # bool | If true, all attribute instances are deleted. Otherwise (default) only the Attribute instance specified by the datasetId is deleted. In case neither the deleteAll flag nor a datasetId is present, the default Attribute instance is deleted.  (optional)
    dataset_id = ngsi_ld_client_1_8_1.QueryEntityDatasetIdParameter() # QueryEntityDatasetIdParameter | Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Attribute delete 
        api_instance.delete_attrs(entity_id, attr_id, delete_all=delete_all, dataset_id=dataset_id, type=type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->delete_attrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **delete_all** | **bool**| If true, all attribute instances are deleted. Otherwise (default) only the Attribute instance specified by the datasetId is deleted. In case neither the deleteAll flag nor a datasetId is present, the default Attribute instance is deleted.  | [optional] 
 **dataset_id** | [**QueryEntityDatasetIdParameter**](.md)| Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
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
**207** | Only the Attributes included in the response payload body were successfully appended. If no Attributes were successfully updated the updated array of UpdateResult (see clause 5.2.18) will be empty.  If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation.  In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a UpdateResult structure.  Names of the Attributes included in the UpdateResult structure are represented as Fully Qualified Names as per clause 6.3.6.  Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_batch**
> delete_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, request_body=request_body)

Batch Entity Delete 

5.6.10 Batch Entity Delete.  This operation allows deleting a batch of NGSI-LD Entities. 

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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    request_body = ['request_body_example'] # List[str] | Array of String (URIs representing Entity IDs) to be deleted.  (optional)

    try:
        # Batch Entity Delete 
        api_instance.delete_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, request_body=request_body)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->delete_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **request_body** | [**List[str]**](str.md)| Array of String (URIs representing Entity IDs) to be deleted.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | If all entities existed and have been successfully deleted, there is no payload body in the response.  |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity**
> delete_entity(entity_id, type=type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Entity deletion by id 

5.6.6 Delete entity.  This operation allows deleting an NGSI-LD Entity. 

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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Entity deletion by id 
        api_instance.delete_entity(entity_id, type=type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
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
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_batch**
> merge_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)

Batch Entity Merge 

5.6.20 Batch Entity Merge.  This operation allows modification of a batch of NGSI-LD Entities according to the JSON Merge Patch processing rules defined in IETF RFC 7396 by adding new attributes (Properties or Relationships) or modifying or deleting existing attributes associated with an existing Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    query_entity200_response_inner = [ngsi_ld_client_1_8_1.QueryEntity200ResponseInner()] # List[QueryEntity200ResponseInner] | Array of Entities to be merged.  (optional)

    try:
        # Batch Entity Merge 
        api_instance.merge_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->merge_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **query_entity200_response_inner** | [**List[QueryEntity200ResponseInner]**](QueryEntity200ResponseInner.md)| Array of Entities to be merged.  | [optional] 

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
**204** | If all entities have been successfully merged, there is no payload body in the response.  |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_entity**
> merge_entity(entity_id, options=options, format=format, type=type, observed_at=observed_at, lang=lang, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)

Entity merge by id 

5.6.17 Merge Entity.  This operation allows modification of an existing NGSI-LD Entity aligning to the JSON Merge Patch processing rules defined in IETF RFC 7396 by adding new Attributes (Properties or Relationships) or modifying or deleting existing Attributes associated with an existing Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity import Entity
from ngsi_ld_client_1_8_1.models.format_representation import FormatRepresentation
from ngsi_ld_client_1_8_1.models.options_representation import OptionsRepresentation
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    options = [ngsi_ld_client_1_8_1.OptionsRepresentation()] # List[OptionsRepresentation] |  (optional)
    format = ngsi_ld_client_1_8_1.FormatRepresentation() # FormatRepresentation |  (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    observed_at = '2013-10-20T19:20:30+01:00' # datetime | When a merge operation applies to a pre-existing Attribute which previously contained an \"observedAt\" sub-attribute, the value held in this query parameter shall be used if no specific \"observedAt\" sub-Attribute is found in the payload body.  (optional)
    lang = 'lang_example' # str | It is used to reduce languageMaps to a string or string array property in a single preferred language.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity = ngsi_ld_client_1_8_1.Entity() # Entity | Entity Fragment containing a complete representation of the Attributes to be merged.  (optional)

    try:
        # Entity merge by id 
        api_instance.merge_entity(entity_id, options=options, format=format, type=type, observed_at=observed_at, lang=lang, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->merge_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **options** | [**List[OptionsRepresentation]**](OptionsRepresentation.md)|  | [optional] 
 **format** | [**FormatRepresentation**](.md)|  | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **observed_at** | **datetime**| When a merge operation applies to a pre-existing Attribute which previously contained an \&quot;observedAt\&quot; sub-attribute, the value held in this query parameter shall be used if no specific \&quot;observedAt\&quot; sub-Attribute is found in the payload body.  | [optional] 
 **lang** | **str**| It is used to reduce languageMaps to a string or string array property in a single preferred language.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity** | [**Entity**](Entity.md)| Entity Fragment containing a complete representation of the Attributes to be merged.  | [optional] 

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
**204** | All the Attributes were merged successfully.  |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_attrs**
> replace_attrs(entity_id, attr_id, local=local, type=type, link=link, ngsild_tenant=ngsild_tenant, via=via, replace_attrs_request=replace_attrs_request)

Attribute replace 

5.6.19 Attribute Replace.  This operation allows the replacement of a single Attribute (Property or Relationship) within an NGSI-LD Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.replace_attrs_request import ReplaceAttrsRequest
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    replace_attrs_request = ngsi_ld_client_1_8_1.ReplaceAttrsRequest() # ReplaceAttrsRequest |  (optional)

    try:
        # Attribute replace 
        api_instance.replace_attrs(entity_id, attr_id, local=local, type=type, link=link, ngsild_tenant=ngsild_tenant, via=via, replace_attrs_request=replace_attrs_request)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->replace_attrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **replace_attrs_request** | [**ReplaceAttrsRequest**](ReplaceAttrsRequest.md)|  | [optional] 

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
**204** | The attribute was replaced successfully.  |  * NGSILD-Tenant -  <br>  |
**207** | Only the Attributes included in the response payload body were successfully appended. If no Attributes were successfully updated the updated array of UpdateResult (see clause 5.2.18) will be empty.  If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation.  In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a UpdateResult structure.  Names of the Attributes included in the UpdateResult structure are represented as Fully Qualified Names as per clause 6.3.6.  Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_entity**
> replace_entity(entity_id, type=type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)

Entity replacement by id 

5.6.18 Replace Entity.  This operation allows the modification of an existing NGSI-LD Entity by replacing all of the Attributes (Properties or Relationships). 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity import Entity
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity = ngsi_ld_client_1_8_1.Entity() # Entity | Entity Fragment containing a complete representation of the Entity to be replaced.  (optional)

    try:
        # Entity replacement by id 
        api_instance.replace_entity(entity_id, type=type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->replace_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity** | [**Entity**](Entity.md)| Entity Fragment containing a complete representation of the Entity to be replaced.  | [optional] 

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
**204** | The entity was replaced successfully.  |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attrs**
> update_attrs(entity_id, attr_id, local=local, type=type, link=link, ngsild_tenant=ngsild_tenant, via=via, replace_attrs_request=replace_attrs_request)

Partial Attribute Update 

5.6.4 Partial Attribute Update.  This operation allows performing a partial update on an NGSI-LD Entity's Attribute (Property or Relationship). A partial update only changes the elements provided in an Entity Fragment, leaving the rest as they are. This operation supports the deletion of sub-Attributes but not the deletion of the whole Attribute itself. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.replace_attrs_request import ReplaceAttrsRequest
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    replace_attrs_request = ngsi_ld_client_1_8_1.ReplaceAttrsRequest() # ReplaceAttrsRequest |  (optional)

    try:
        # Partial Attribute Update 
        api_instance.update_attrs(entity_id, attr_id, local=local, type=type, link=link, ngsild_tenant=ngsild_tenant, via=via, replace_attrs_request=replace_attrs_request)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->update_attrs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **replace_attrs_request** | [**ReplaceAttrsRequest**](ReplaceAttrsRequest.md)|  | [optional] 

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
**207** | Only the Attributes included in the response payload body were successfully appended. If no Attributes were successfully updated the updated array of UpdateResult (see clause 5.2.18) will be empty.  If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation.  In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a UpdateResult structure.  Names of the Attributes included in the UpdateResult structure are represented as Fully Qualified Names as per clause 6.3.6.  Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_batch**
> update_batch(options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)

Batch Entity Update 

5.6.9 Batch Entity Update.  This operation allows updating a batch of NGSI-LD Entities. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.options_no_overwrite import OptionsNoOverwrite
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    options = [ngsi_ld_client_1_8_1.OptionsNoOverwrite()] # List[OptionsNoOverwrite] |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    query_entity200_response_inner = [ngsi_ld_client_1_8_1.QueryEntity200ResponseInner()] # List[QueryEntity200ResponseInner] | Array of entities to be updated.  (optional)

    try:
        # Batch Entity Update 
        api_instance.update_batch(options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->update_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**List[OptionsNoOverwrite]**](OptionsNoOverwrite.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **query_entity200_response_inner** | [**List[QueryEntity200ResponseInner]**](QueryEntity200ResponseInner.md)| Array of entities to be updated.  | [optional] 

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
**204** | If all entities have been successfully updated, there is no payload body in the response.   |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity**
> update_entity(entity_id, local=local, type=type, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)

Update Attributes of an Entity 

5.6.2 Update Entity Attributes.  This operation allows modifying an existing NGSI-LD Entity by updating already existing Attributes (Properties or Relationships). 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity import Entity
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    entity = ngsi_ld_client_1_8_1.Entity() # Entity | Entity Fragment containing a complete representation of the Attributes to be updated.  (optional)

    try:
        # Update Attributes of an Entity 
        api_instance.update_entity(entity_id, local=local, type=type, link=link, ngsild_tenant=ngsild_tenant, via=via, entity=entity)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->update_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **entity** | [**Entity**](Entity.md)| Entity Fragment containing a complete representation of the Attributes to be updated.  | [optional] 

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
**204** | All the Attributes were appended successfully.  |  * NGSILD-Tenant -  <br>  |
**207** | Only the Attributes included in the response payload body were successfully appended. If no Attributes were successfully updated the updated array of UpdateResult (see clause 5.2.18) will be empty.  If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation.  In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a UpdateResult structure.  Names of the Attributes included in the UpdateResult structure are represented as Fully Qualified Names as per clause 6.3.6.  Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_batch**
> List[str] upsert_batch(options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)

Batch Entity Creation or Update (Upsert) 

5.6.8 Batch Entity Upsert.  This operation allows creating a batch of NGSI-LD Entities, updating each of them if they already existed. In some database jargon this kind of operation is known as \"upsert\". 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.options_upsert import OptionsUpsert
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextInformationProvisionApi(api_client)
    options = [ngsi_ld_client_1_8_1.OptionsUpsert()] # List[OptionsUpsert] |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    query_entity200_response_inner = [ngsi_ld_client_1_8_1.QueryEntity200ResponseInner()] # List[QueryEntity200ResponseInner] | Array of entities to be created.  (optional)

    try:
        # Batch Entity Creation or Update (Upsert) 
        api_response = api_instance.upsert_batch(options=options, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via, query_entity200_response_inner=query_entity200_response_inner)
        print("The response of ContextInformationProvisionApi->upsert_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationProvisionApi->upsert_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**List[OptionsUpsert]**](OptionsUpsert.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **query_entity200_response_inner** | [**List[QueryEntity200ResponseInner]**](QueryEntity200ResponseInner.md)| Array of entities to be created.  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | If all entities not existing prior to this request have been successfully created and the others have been successfully updated, an array of String (with the URIs representing the Entity Ids of the created entities only) is returned in the response. There is no restriction as to the order of the Entity Ids. The merely updated entities do not take part in the response (corresponding to 204 No Content returned in the case of updates).  |  * NGSILD-Tenant -  <br>  |
**204** | If all entities already existed and are successfully updated, there is no payload body in the response.  |  * NGSILD-Tenant -  <br>  |
**207** | If the entity input data matches to a registration, the relevant parts of the request are forwarded as a distributed operation. In the case when an error response is received back from any distributed operation, a response body containing the result returned from each registration is returned in a BatchOperationResult structure. Errors can occur whenever a distributed operation is unsupported, fails or times out, see clause 6.3.17.  |  * NGSILD-Tenant -  <br>  * Location -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

