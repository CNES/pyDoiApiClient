# swagger_client.DataCiteMetadataStoreMDSAPIApi

All URIs are relative to *https://localhost:8183*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_doi_project**](DataCiteMetadataStoreMDSAPIApi.md#cancel_doi_project) | **DELETE** /mds/metadata/{prefix}/{project}/{doi_name} | 
[**get_all_doi_metadata**](DataCiteMetadataStoreMDSAPIApi.md#get_all_doi_metadata) | **GET** /mds/metadata/{prefix}/{project}/{doi_name} | 
[**get_doi_media**](DataCiteMetadataStoreMDSAPIApi.md#get_doi_media) | **GET** /mds/media/{prefix}/{project}/{doi_name} | 
[**get_landing_page_url**](DataCiteMetadataStoreMDSAPIApi.md#get_landing_page_url) | **GET** /mds/dois/{prefix}/{project}/{doi_name} | 
[**post_doi_metadata**](DataCiteMetadataStoreMDSAPIApi.md#post_doi_metadata) | **POST** /mds/metadata | 
[**post_landing_page**](DataCiteMetadataStoreMDSAPIApi.md#post_landing_page) | **POST** /mds/dois | 
[**post_media**](DataCiteMetadataStoreMDSAPIApi.md#post_media) | **POST** /mds/media/{prefix}/{project}/{doi_name} | 


# **cancel_doi_project**
> object cancel_doi_project(prefix, project, doi_name, selected_role=selected_role)



This request marks a dataset as 'inactive'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi(swagger_client.ApiClient(configuration))
prefix = 'prefix_example' # str | DOI prefix
project = 'project_example' # str | Project identifier
doi_name = 'doi_name_example' # str | Record ID
selected_role = 'selected_role_example' # str | the selected role when a user is connected to more than 2 roles. (optional)

try:
    api_response = api_instance.cancel_doi_project(prefix, project, doi_name, selected_role=selected_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->cancel_doi_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| DOI prefix | 
 **project** | **str**| Project identifier | 
 **doi_name** | **str**| Record ID | 
 **selected_role** | **str**| the selected role when a user is connected to more than 2 roles. | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_doi_metadata**
> object get_all_doi_metadata(prefix, project, doi_name)



Get all metdata oi

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi()
prefix = 'prefix_example' # str | DOI prefix
project = 'project_example' # str | Project identifier
doi_name = 'doi_name_example' # str | Record ID

try:
    api_response = api_instance.get_all_doi_metadata(prefix, project, doi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->get_all_doi_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| DOI prefix | 
 **project** | **str**| Project identifier | 
 **doi_name** | **str**| Record ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doi_media**
> list[str] get_doi_media(prefix, project, doi_name, selected_role=selected_role)



Retuen a list of pairs of media type and URLs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi()
prefix = 'prefix_example' # str | DOI prefix
project = 'project_example' # str | Project identifier
doi_name = 'doi_name_example' # str | Record ID
selected_role = 'selected_role_example' # str | the selected role when a user is connected to more than 2 roles. (optional)

try:
    api_response = api_instance.get_doi_media(prefix, project, doi_name, selected_role=selected_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->get_doi_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| DOI prefix | 
 **project** | **str**| Project identifier | 
 **doi_name** | **str**| Record ID | 
 **selected_role** | **str**| the selected role when a user is connected to more than 2 roles. | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/uri-list

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_landing_page_url**
> str get_landing_page_url(prefix, project, doi_name)



Retrieves the landing page URL

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi()
prefix = 'prefix_example' # str | DOI prefix
project = 'project_example' # str | Project identifier
doi_name = 'doi_name_example' # str | Record ID

try:
    api_response = api_instance.get_landing_page_url(prefix, project, doi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->get_landing_page_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| DOI prefix | 
 **project** | **str**| Project identifier | 
 **doi_name** | **str**| Record ID | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doi_metadata**
> str post_doi_metadata(body, selected_role=selected_role)



Create or update doi project metadata (short explanation of status code e.g. CREATED, HANDLE_ALREADY_EXISTS)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | metadata
selected_role = 'selected_role_example' # str | the selected role when a user is connected to more than 2 roles. (optional)

try:
    api_response = api_instance.post_doi_metadata(body, selected_role=selected_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->post_doi_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| metadata | 
 **selected_role** | **str**| the selected role when a user is connected to more than 2 roles. | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_landing_page**
> str post_landing_page(url, doi, selected_role=selected_role)



Create a **new** doi project or update the landing page url if it the project already exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi(swagger_client.ApiClient(configuration))
url = 'url_example' # str | the URL of the landing page
doi = 'doi_example' # str | the project suffix, which is an unique identifier within the project
selected_role = 'selected_role_example' # str | the selected role when a user is connected to more than 2 roles. (optional)

try:
    api_response = api_instance.post_landing_page(url, doi, selected_role=selected_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->post_landing_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| the URL of the landing page | 
 **doi** | **str**| the project suffix, which is an unique identifier within the project | 
 **selected_role** | **str**| the selected role when a user is connected to more than 2 roles. | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_media**
> str post_media(prefix, project, doi_name, selected_role=selected_role)



add an association media/url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataCiteMetadataStoreMDSAPIApi(swagger_client.ApiClient(configuration))
prefix = 'prefix_example' # str | DOI prefix
project = 'project_example' # str | Project identifier
doi_name = 'doi_name_example' # str | Record ID
selected_role = 'selected_role_example' # str | the selected role when a user is connected to more than 2 roles. (optional)

try:
    api_response = api_instance.post_media(prefix, project, doi_name, selected_role=selected_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataCiteMetadataStoreMDSAPIApi->post_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| DOI prefix | 
 **project** | **str**| Project identifier | 
 **doi_name** | **str**| Record ID | 
 **selected_role** | **str**| the selected role when a user is connected to more than 2 roles. | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

