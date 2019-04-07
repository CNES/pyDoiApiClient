# swagger_client.AdministrationApi

All URIs are relative to *https://localhost:8183*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](AdministrationApi.md#create_token) | **POST** /admin/token | 


# **create_token**
> str create_token()



Create a token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.create_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->create_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

