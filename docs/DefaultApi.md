# opcua_webapi.DefaultApi

All URIs are relative to *http://localhost:4840*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_session**](DefaultApi.md#activate_session) | **POST** /activatesession | 
[**browse**](DefaultApi.md#browse) | **POST** /browse | 
[**browse_next**](DefaultApi.md#browse_next) | **POST** /browsenext | 
[**call**](DefaultApi.md#call) | **POST** /call | 
[**cancel**](DefaultApi.md#cancel) | **POST** /cancel | 
[**close_session**](DefaultApi.md#close_session) | **POST** /closesession | 
[**create_monitored_items**](DefaultApi.md#create_monitored_items) | **POST** /createmonitoreditems | 
[**create_session**](DefaultApi.md#create_session) | **POST** /createsession | 
[**create_subscription**](DefaultApi.md#create_subscription) | **POST** /createsubscription | 
[**delete_monitored_items**](DefaultApi.md#delete_monitored_items) | **POST** /deletemonitoreditems | 
[**delete_subscriptions**](DefaultApi.md#delete_subscriptions) | **POST** /deletesubscriptions | 
[**find_servers**](DefaultApi.md#find_servers) | **POST** /findservers | 
[**get_endpoints**](DefaultApi.md#get_endpoints) | **POST** /getendpoints | 
[**history_read**](DefaultApi.md#history_read) | **POST** /historyread | 
[**history_update**](DefaultApi.md#history_update) | **POST** /historyupdate | 
[**modify_monitored_items**](DefaultApi.md#modify_monitored_items) | **POST** /modifymonitoreditems | 
[**modify_subscription**](DefaultApi.md#modify_subscription) | **POST** /modifysubscription | 
[**publish**](DefaultApi.md#publish) | **POST** /publish | 
[**read**](DefaultApi.md#read) | **POST** /read | 
[**register_nodes**](DefaultApi.md#register_nodes) | **POST** /registernodes | 
[**republish**](DefaultApi.md#republish) | **POST** /republish | 
[**set_monitoring_mode**](DefaultApi.md#set_monitoring_mode) | **POST** /setmonitoringmode | 
[**set_publishing_mode**](DefaultApi.md#set_publishing_mode) | **POST** /setpublishingmode | 
[**set_triggering**](DefaultApi.md#set_triggering) | **POST** /settriggering | 
[**transfer_subscriptions**](DefaultApi.md#transfer_subscriptions) | **POST** /transfersubscriptions | 
[**translate_browse_paths_to_node_ids**](DefaultApi.md#translate_browse_paths_to_node_ids) | **POST** /translate | 
[**unregister_nodes**](DefaultApi.md#unregister_nodes) | **POST** /unregisternodes | 
[**write**](DefaultApi.md#write) | **POST** /write | 


# **activate_session**
> ActivateSessionResponse activate_session(activate_session_request=activate_session_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.activate_session_request import ActivateSessionRequest
from opcua_webapi.models.activate_session_response import ActivateSessionResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    activate_session_request = opcua_webapi.ActivateSessionRequest() # ActivateSessionRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.3/#5.7.3.2). (optional)

    try:
        api_response = api_instance.activate_session(activate_session_request=activate_session_request)
        print("The response of DefaultApi->activate_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->activate_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_session_request** | [**ActivateSessionRequest**](ActivateSessionRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.3/#5.7.3.2). | [optional] 

### Return type

[**ActivateSessionResponse**](ActivateSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.3/#5.7.3.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **browse**
> BrowseResponse browse(browse_request=browse_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.browse_request import BrowseRequest
from opcua_webapi.models.browse_response import BrowseResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    browse_request = opcua_webapi.BrowseRequest() # BrowseRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.2/#5.9.2.2). (optional)

    try:
        api_response = api_instance.browse(browse_request=browse_request)
        print("The response of DefaultApi->browse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->browse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browse_request** | [**BrowseRequest**](BrowseRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.2/#5.9.2.2). | [optional] 

### Return type

[**BrowseResponse**](BrowseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.2/#5.9.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **browse_next**
> BrowseNextResponse browse_next(browse_next_request=browse_next_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.browse_next_request import BrowseNextRequest
from opcua_webapi.models.browse_next_response import BrowseNextResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    browse_next_request = opcua_webapi.BrowseNextRequest() # BrowseNextRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.3/#5.9.3.2). (optional)

    try:
        api_response = api_instance.browse_next(browse_next_request=browse_next_request)
        print("The response of DefaultApi->browse_next:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->browse_next: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browse_next_request** | [**BrowseNextRequest**](BrowseNextRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.3/#5.9.3.2). | [optional] 

### Return type

[**BrowseNextResponse**](BrowseNextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.3/#5.9.3.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call**
> CallResponse call(call_request=call_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.call_request import CallRequest
from opcua_webapi.models.call_response import CallResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    call_request = opcua_webapi.CallRequest() # CallRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.12.2/#5.12.2.2). (optional)

    try:
        api_response = api_instance.call(call_request=call_request)
        print("The response of DefaultApi->call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_request** | [**CallRequest**](CallRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.12.2/#5.12.2.2). | [optional] 

### Return type

[**CallResponse**](CallResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.12.2/#5.12.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel**
> CancelResponse cancel(cancel_request=cancel_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.cancel_request import CancelRequest
from opcua_webapi.models.cancel_response import CancelResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    cancel_request = opcua_webapi.CancelRequest() # CancelRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.5/#5.7.5.2). (optional)

    try:
        api_response = api_instance.cancel(cancel_request=cancel_request)
        print("The response of DefaultApi->cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_request** | [**CancelRequest**](CancelRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.5/#5.7.5.2). | [optional] 

### Return type

[**CancelResponse**](CancelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.5/#5.7.5.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_session**
> CloseSessionResponse close_session(close_session_request=close_session_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.close_session_request import CloseSessionRequest
from opcua_webapi.models.close_session_response import CloseSessionResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    close_session_request = opcua_webapi.CloseSessionRequest() # CloseSessionRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.4/#5.7.4.2). (optional)

    try:
        api_response = api_instance.close_session(close_session_request=close_session_request)
        print("The response of DefaultApi->close_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->close_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_session_request** | [**CloseSessionRequest**](CloseSessionRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.4/#5.7.4.2). | [optional] 

### Return type

[**CloseSessionResponse**](CloseSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.4/#5.7.4.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_monitored_items**
> CreateMonitoredItemsResponse create_monitored_items(create_monitored_items_request=create_monitored_items_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.create_monitored_items_request import CreateMonitoredItemsRequest
from opcua_webapi.models.create_monitored_items_response import CreateMonitoredItemsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    create_monitored_items_request = opcua_webapi.CreateMonitoredItemsRequest() # CreateMonitoredItemsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.2/#5.13.2.2). (optional)

    try:
        api_response = api_instance.create_monitored_items(create_monitored_items_request=create_monitored_items_request)
        print("The response of DefaultApi->create_monitored_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_monitored_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_monitored_items_request** | [**CreateMonitoredItemsRequest**](CreateMonitoredItemsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.2/#5.13.2.2). | [optional] 

### Return type

[**CreateMonitoredItemsResponse**](CreateMonitoredItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.2/#5.13.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> CreateSessionResponse create_session(create_session_request=create_session_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.create_session_request import CreateSessionRequest
from opcua_webapi.models.create_session_response import CreateSessionResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    create_session_request = opcua_webapi.CreateSessionRequest() # CreateSessionRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.2/#5.7.2.2). (optional)

    try:
        api_response = api_instance.create_session(create_session_request=create_session_request)
        print("The response of DefaultApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_session_request** | [**CreateSessionRequest**](CreateSessionRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.2/#5.7.2.2). | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.7.2/#5.7.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> CreateSubscriptionResponse create_subscription(create_subscription_request=create_subscription_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.create_subscription_request import CreateSubscriptionRequest
from opcua_webapi.models.create_subscription_response import CreateSubscriptionResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    create_subscription_request = opcua_webapi.CreateSubscriptionRequest() # CreateSubscriptionRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.2/#5.14.2.2). (optional)

    try:
        api_response = api_instance.create_subscription(create_subscription_request=create_subscription_request)
        print("The response of DefaultApi->create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_request** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.2/#5.14.2.2). | [optional] 

### Return type

[**CreateSubscriptionResponse**](CreateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.2/#5.14.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitored_items**
> DeleteMonitoredItemsResponse delete_monitored_items(delete_monitored_items_request=delete_monitored_items_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.delete_monitored_items_request import DeleteMonitoredItemsRequest
from opcua_webapi.models.delete_monitored_items_response import DeleteMonitoredItemsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    delete_monitored_items_request = opcua_webapi.DeleteMonitoredItemsRequest() # DeleteMonitoredItemsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.6/#5.13.6.2). (optional)

    try:
        api_response = api_instance.delete_monitored_items(delete_monitored_items_request=delete_monitored_items_request)
        print("The response of DefaultApi->delete_monitored_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_monitored_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_monitored_items_request** | [**DeleteMonitoredItemsRequest**](DeleteMonitoredItemsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.6/#5.13.6.2). | [optional] 

### Return type

[**DeleteMonitoredItemsResponse**](DeleteMonitoredItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.6/#5.13.6.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriptions**
> DeleteSubscriptionsResponse delete_subscriptions(delete_subscriptions_request=delete_subscriptions_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.delete_subscriptions_request import DeleteSubscriptionsRequest
from opcua_webapi.models.delete_subscriptions_response import DeleteSubscriptionsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    delete_subscriptions_request = opcua_webapi.DeleteSubscriptionsRequest() # DeleteSubscriptionsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.8/#5.14.8.2). (optional)

    try:
        api_response = api_instance.delete_subscriptions(delete_subscriptions_request=delete_subscriptions_request)
        print("The response of DefaultApi->delete_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_subscriptions_request** | [**DeleteSubscriptionsRequest**](DeleteSubscriptionsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.8/#5.14.8.2). | [optional] 

### Return type

[**DeleteSubscriptionsResponse**](DeleteSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.8/#5.14.8.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_servers**
> FindServersResponse find_servers(find_servers_request=find_servers_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.find_servers_request import FindServersRequest
from opcua_webapi.models.find_servers_response import FindServersResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    find_servers_request = opcua_webapi.FindServersRequest() # FindServersRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.5.2/#5.5.2.2). (optional)

    try:
        api_response = api_instance.find_servers(find_servers_request=find_servers_request)
        print("The response of DefaultApi->find_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->find_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_servers_request** | [**FindServersRequest**](FindServersRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.5.2/#5.5.2.2). | [optional] 

### Return type

[**FindServersResponse**](FindServersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.5.2/#5.5.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints**
> GetEndpointsResponse get_endpoints(get_endpoints_request=get_endpoints_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.get_endpoints_request import GetEndpointsRequest
from opcua_webapi.models.get_endpoints_response import GetEndpointsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    get_endpoints_request = opcua_webapi.GetEndpointsRequest() # GetEndpointsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.5.4/#5.5.4.2). (optional)

    try:
        api_response = api_instance.get_endpoints(get_endpoints_request=get_endpoints_request)
        print("The response of DefaultApi->get_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_endpoints_request** | [**GetEndpointsRequest**](GetEndpointsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.5.4/#5.5.4.2). | [optional] 

### Return type

[**GetEndpointsResponse**](GetEndpointsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.5.4/#5.5.4.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_read**
> HistoryReadResponse history_read(history_read_request=history_read_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.history_read_request import HistoryReadRequest
from opcua_webapi.models.history_read_response import HistoryReadResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    history_read_request = opcua_webapi.HistoryReadRequest() # HistoryReadRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.3/#5.11.3.2). (optional)

    try:
        api_response = api_instance.history_read(history_read_request=history_read_request)
        print("The response of DefaultApi->history_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->history_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_read_request** | [**HistoryReadRequest**](HistoryReadRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.3/#5.11.3.2). | [optional] 

### Return type

[**HistoryReadResponse**](HistoryReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.3/#5.11.3.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_update**
> HistoryUpdateResponse history_update(history_update_request=history_update_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.history_update_request import HistoryUpdateRequest
from opcua_webapi.models.history_update_response import HistoryUpdateResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    history_update_request = opcua_webapi.HistoryUpdateRequest() # HistoryUpdateRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.5/#5.11.5.2). (optional)

    try:
        api_response = api_instance.history_update(history_update_request=history_update_request)
        print("The response of DefaultApi->history_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->history_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_update_request** | [**HistoryUpdateRequest**](HistoryUpdateRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.5/#5.11.5.2). | [optional] 

### Return type

[**HistoryUpdateResponse**](HistoryUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.5/#5.11.5.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_monitored_items**
> ModifyMonitoredItemsResponse modify_monitored_items(modify_monitored_items_request=modify_monitored_items_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.modify_monitored_items_request import ModifyMonitoredItemsRequest
from opcua_webapi.models.modify_monitored_items_response import ModifyMonitoredItemsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    modify_monitored_items_request = opcua_webapi.ModifyMonitoredItemsRequest() # ModifyMonitoredItemsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.3/#5.13.3.2). (optional)

    try:
        api_response = api_instance.modify_monitored_items(modify_monitored_items_request=modify_monitored_items_request)
        print("The response of DefaultApi->modify_monitored_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->modify_monitored_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_monitored_items_request** | [**ModifyMonitoredItemsRequest**](ModifyMonitoredItemsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.3/#5.13.3.2). | [optional] 

### Return type

[**ModifyMonitoredItemsResponse**](ModifyMonitoredItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.3/#5.13.3.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_subscription**
> ModifySubscriptionResponse modify_subscription(modify_subscription_request=modify_subscription_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.modify_subscription_request import ModifySubscriptionRequest
from opcua_webapi.models.modify_subscription_response import ModifySubscriptionResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    modify_subscription_request = opcua_webapi.ModifySubscriptionRequest() # ModifySubscriptionRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.3/#5.14.3.2). (optional)

    try:
        api_response = api_instance.modify_subscription(modify_subscription_request=modify_subscription_request)
        print("The response of DefaultApi->modify_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->modify_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_subscription_request** | [**ModifySubscriptionRequest**](ModifySubscriptionRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.3/#5.14.3.2). | [optional] 

### Return type

[**ModifySubscriptionResponse**](ModifySubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.3/#5.14.3.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> PublishResponse publish(publish_request=publish_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.publish_request import PublishRequest
from opcua_webapi.models.publish_response import PublishResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    publish_request = opcua_webapi.PublishRequest() # PublishRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.5/#5.14.5.2). (optional)

    try:
        api_response = api_instance.publish(publish_request=publish_request)
        print("The response of DefaultApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_request** | [**PublishRequest**](PublishRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.5/#5.14.5.2). | [optional] 

### Return type

[**PublishResponse**](PublishResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.5/#5.14.5.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ReadResponse read(read_request=read_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.read_request import ReadRequest
from opcua_webapi.models.read_response import ReadResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    read_request = opcua_webapi.ReadRequest() # ReadRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.2/#5.11.2.2). (optional)

    try:
        api_response = api_instance.read(read_request=read_request)
        print("The response of DefaultApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_request** | [**ReadRequest**](ReadRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.2/#5.11.2.2). | [optional] 

### Return type

[**ReadResponse**](ReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.2/#5.11.2.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_nodes**
> RegisterNodesResponse register_nodes(register_nodes_request=register_nodes_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.register_nodes_request import RegisterNodesRequest
from opcua_webapi.models.register_nodes_response import RegisterNodesResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    register_nodes_request = opcua_webapi.RegisterNodesRequest() # RegisterNodesRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.5/#5.9.5.2). (optional)

    try:
        api_response = api_instance.register_nodes(register_nodes_request=register_nodes_request)
        print("The response of DefaultApi->register_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_nodes_request** | [**RegisterNodesRequest**](RegisterNodesRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.5/#5.9.5.2). | [optional] 

### Return type

[**RegisterNodesResponse**](RegisterNodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.5/#5.9.5.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **republish**
> RepublishResponse republish(republish_request=republish_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.republish_request import RepublishRequest
from opcua_webapi.models.republish_response import RepublishResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    republish_request = opcua_webapi.RepublishRequest() # RepublishRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.6/#5.14.6.2). (optional)

    try:
        api_response = api_instance.republish(republish_request=republish_request)
        print("The response of DefaultApi->republish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->republish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **republish_request** | [**RepublishRequest**](RepublishRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.6/#5.14.6.2). | [optional] 

### Return type

[**RepublishResponse**](RepublishResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.6/#5.14.6.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_monitoring_mode**
> SetMonitoringModeResponse set_monitoring_mode(set_monitoring_mode_request=set_monitoring_mode_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.set_monitoring_mode_request import SetMonitoringModeRequest
from opcua_webapi.models.set_monitoring_mode_response import SetMonitoringModeResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    set_monitoring_mode_request = opcua_webapi.SetMonitoringModeRequest() # SetMonitoringModeRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.4/#5.13.4.2). (optional)

    try:
        api_response = api_instance.set_monitoring_mode(set_monitoring_mode_request=set_monitoring_mode_request)
        print("The response of DefaultApi->set_monitoring_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_monitoring_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_monitoring_mode_request** | [**SetMonitoringModeRequest**](SetMonitoringModeRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.4/#5.13.4.2). | [optional] 

### Return type

[**SetMonitoringModeResponse**](SetMonitoringModeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.4/#5.13.4.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_publishing_mode**
> SetPublishingModeResponse set_publishing_mode(set_publishing_mode_request=set_publishing_mode_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.set_publishing_mode_request import SetPublishingModeRequest
from opcua_webapi.models.set_publishing_mode_response import SetPublishingModeResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    set_publishing_mode_request = opcua_webapi.SetPublishingModeRequest() # SetPublishingModeRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.4/#5.14.4.2). (optional)

    try:
        api_response = api_instance.set_publishing_mode(set_publishing_mode_request=set_publishing_mode_request)
        print("The response of DefaultApi->set_publishing_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_publishing_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_publishing_mode_request** | [**SetPublishingModeRequest**](SetPublishingModeRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.4/#5.14.4.2). | [optional] 

### Return type

[**SetPublishingModeResponse**](SetPublishingModeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.4/#5.14.4.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_triggering**
> SetTriggeringResponse set_triggering(set_triggering_request=set_triggering_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.set_triggering_request import SetTriggeringRequest
from opcua_webapi.models.set_triggering_response import SetTriggeringResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    set_triggering_request = opcua_webapi.SetTriggeringRequest() # SetTriggeringRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.5/#5.13.5.2). (optional)

    try:
        api_response = api_instance.set_triggering(set_triggering_request=set_triggering_request)
        print("The response of DefaultApi->set_triggering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_triggering: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_triggering_request** | [**SetTriggeringRequest**](SetTriggeringRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.5/#5.13.5.2). | [optional] 

### Return type

[**SetTriggeringResponse**](SetTriggeringResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.5/#5.13.5.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_subscriptions**
> TransferSubscriptionsResponse transfer_subscriptions(transfer_subscriptions_request=transfer_subscriptions_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.transfer_subscriptions_request import TransferSubscriptionsRequest
from opcua_webapi.models.transfer_subscriptions_response import TransferSubscriptionsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    transfer_subscriptions_request = opcua_webapi.TransferSubscriptionsRequest() # TransferSubscriptionsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.7/#5.14.7.2). (optional)

    try:
        api_response = api_instance.transfer_subscriptions(transfer_subscriptions_request=transfer_subscriptions_request)
        print("The response of DefaultApi->transfer_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->transfer_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_subscriptions_request** | [**TransferSubscriptionsRequest**](TransferSubscriptionsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.7/#5.14.7.2). | [optional] 

### Return type

[**TransferSubscriptionsResponse**](TransferSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.7/#5.14.7.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_browse_paths_to_node_ids**
> TranslateBrowsePathsToNodeIdsResponse translate_browse_paths_to_node_ids(translate_browse_paths_to_node_ids_request=translate_browse_paths_to_node_ids_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.translate_browse_paths_to_node_ids_request import TranslateBrowsePathsToNodeIdsRequest
from opcua_webapi.models.translate_browse_paths_to_node_ids_response import TranslateBrowsePathsToNodeIdsResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    translate_browse_paths_to_node_ids_request = opcua_webapi.TranslateBrowsePathsToNodeIdsRequest() # TranslateBrowsePathsToNodeIdsRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.4/#5.9.4.2). (optional)

    try:
        api_response = api_instance.translate_browse_paths_to_node_ids(translate_browse_paths_to_node_ids_request=translate_browse_paths_to_node_ids_request)
        print("The response of DefaultApi->translate_browse_paths_to_node_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->translate_browse_paths_to_node_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_browse_paths_to_node_ids_request** | [**TranslateBrowsePathsToNodeIdsRequest**](TranslateBrowsePathsToNodeIdsRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.4/#5.9.4.2). | [optional] 

### Return type

[**TranslateBrowsePathsToNodeIdsResponse**](TranslateBrowsePathsToNodeIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.4/#5.9.4.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_nodes**
> UnregisterNodesResponse unregister_nodes(unregister_nodes_request=unregister_nodes_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.unregister_nodes_request import UnregisterNodesRequest
from opcua_webapi.models.unregister_nodes_response import UnregisterNodesResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    unregister_nodes_request = opcua_webapi.UnregisterNodesRequest() # UnregisterNodesRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.6/#5.9.6.2). (optional)

    try:
        api_response = api_instance.unregister_nodes(unregister_nodes_request=unregister_nodes_request)
        print("The response of DefaultApi->unregister_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->unregister_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unregister_nodes_request** | [**UnregisterNodesRequest**](UnregisterNodesRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.6/#5.9.6.2). | [optional] 

### Return type

[**UnregisterNodesResponse**](UnregisterNodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.9.6/#5.9.6.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write**
> WriteResponse write(write_request=write_request)

### Example


```python
import opcua_webapi
from opcua_webapi.models.write_request import WriteRequest
from opcua_webapi.models.write_response import WriteResponse
from opcua_webapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4840
# See configuration.py for a list of all supported configuration parameters.
configuration = opcua_webapi.Configuration(
    host = "http://localhost:4840"
)


# Enter a context with an instance of the API client
with opcua_webapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opcua_webapi.DefaultApi(api_client)
    write_request = opcua_webapi.WriteRequest() # WriteRequest | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.4/#5.11.4.2). (optional)

    try:
        api_response = api_instance.write(write_request=write_request)
        print("The response of DefaultApi->write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **write_request** | [**WriteRequest**](WriteRequest.md)| [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.4/#5.11.4.2). | [optional] 

### Return type

[**WriteResponse**](WriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.4/#5.11.4.2). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

