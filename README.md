# opcua-webapi
Provides simple HTTPS based access to an OPC UA server.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.05.4
- Package version: 1.504.1
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import opcua_webapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import opcua_webapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import opcua_webapi
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
    except ApiException as e:
        print("Exception when calling DefaultApi->activate_session: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:4840*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**activate_session**](docs/DefaultApi.md#activate_session) | **POST** /activatesession | 
*DefaultApi* | [**browse**](docs/DefaultApi.md#browse) | **POST** /browse | 
*DefaultApi* | [**browse_next**](docs/DefaultApi.md#browse_next) | **POST** /browsenext | 
*DefaultApi* | [**call**](docs/DefaultApi.md#call) | **POST** /call | 
*DefaultApi* | [**cancel**](docs/DefaultApi.md#cancel) | **POST** /cancel | 
*DefaultApi* | [**close_session**](docs/DefaultApi.md#close_session) | **POST** /closesession | 
*DefaultApi* | [**create_monitored_items**](docs/DefaultApi.md#create_monitored_items) | **POST** /createmonitoreditems | 
*DefaultApi* | [**create_session**](docs/DefaultApi.md#create_session) | **POST** /createsession | 
*DefaultApi* | [**create_subscription**](docs/DefaultApi.md#create_subscription) | **POST** /createsubscription | 
*DefaultApi* | [**delete_monitored_items**](docs/DefaultApi.md#delete_monitored_items) | **POST** /deletemonitoreditems | 
*DefaultApi* | [**delete_subscriptions**](docs/DefaultApi.md#delete_subscriptions) | **POST** /deletesubscriptions | 
*DefaultApi* | [**find_servers**](docs/DefaultApi.md#find_servers) | **POST** /findservers | 
*DefaultApi* | [**get_endpoints**](docs/DefaultApi.md#get_endpoints) | **POST** /getendpoints | 
*DefaultApi* | [**history_read**](docs/DefaultApi.md#history_read) | **POST** /historyread | 
*DefaultApi* | [**history_update**](docs/DefaultApi.md#history_update) | **POST** /historyupdate | 
*DefaultApi* | [**modify_monitored_items**](docs/DefaultApi.md#modify_monitored_items) | **POST** /modifymonitoreditems | 
*DefaultApi* | [**modify_subscription**](docs/DefaultApi.md#modify_subscription) | **POST** /modifysubscription | 
*DefaultApi* | [**publish**](docs/DefaultApi.md#publish) | **POST** /publish | 
*DefaultApi* | [**read**](docs/DefaultApi.md#read) | **POST** /read | 
*DefaultApi* | [**register_nodes**](docs/DefaultApi.md#register_nodes) | **POST** /registernodes | 
*DefaultApi* | [**republish**](docs/DefaultApi.md#republish) | **POST** /republish | 
*DefaultApi* | [**set_monitoring_mode**](docs/DefaultApi.md#set_monitoring_mode) | **POST** /setmonitoringmode | 
*DefaultApi* | [**set_publishing_mode**](docs/DefaultApi.md#set_publishing_mode) | **POST** /setpublishingmode | 
*DefaultApi* | [**set_triggering**](docs/DefaultApi.md#set_triggering) | **POST** /settriggering | 
*DefaultApi* | [**transfer_subscriptions**](docs/DefaultApi.md#transfer_subscriptions) | **POST** /transfersubscriptions | 
*DefaultApi* | [**translate_browse_paths_to_node_ids**](docs/DefaultApi.md#translate_browse_paths_to_node_ids) | **POST** /translate | 
*DefaultApi* | [**unregister_nodes**](docs/DefaultApi.md#unregister_nodes) | **POST** /unregisternodes | 
*DefaultApi* | [**write**](docs/DefaultApi.md#write) | **POST** /write | 


## Documentation For Models

 - [ActionMethodDataType](docs/ActionMethodDataType.md)
 - [ActionState](docs/ActionState.md)
 - [ActionTargetDataType](docs/ActionTargetDataType.md)
 - [ActivateSessionRequest](docs/ActivateSessionRequest.md)
 - [ActivateSessionResponse](docs/ActivateSessionResponse.md)
 - [AggregateConfiguration](docs/AggregateConfiguration.md)
 - [AggregateFilter](docs/AggregateFilter.md)
 - [AggregateFilterResult](docs/AggregateFilterResult.md)
 - [ApplicationDescription](docs/ApplicationDescription.md)
 - [ApplicationType](docs/ApplicationType.md)
 - [Argument](docs/Argument.md)
 - [AttributeOperand](docs/AttributeOperand.md)
 - [BrokerConnectionTransportDataType](docs/BrokerConnectionTransportDataType.md)
 - [BrokerDataSetReaderTransportDataType](docs/BrokerDataSetReaderTransportDataType.md)
 - [BrokerDataSetWriterTransportDataType](docs/BrokerDataSetWriterTransportDataType.md)
 - [BrokerTransportQualityOfService](docs/BrokerTransportQualityOfService.md)
 - [BrokerWriterGroupTransportDataType](docs/BrokerWriterGroupTransportDataType.md)
 - [BrowseDescription](docs/BrowseDescription.md)
 - [BrowseDirection](docs/BrowseDirection.md)
 - [BrowseNextRequest](docs/BrowseNextRequest.md)
 - [BrowseNextResponse](docs/BrowseNextResponse.md)
 - [BrowsePath](docs/BrowsePath.md)
 - [BrowsePathResult](docs/BrowsePathResult.md)
 - [BrowsePathTarget](docs/BrowsePathTarget.md)
 - [BrowseRequest](docs/BrowseRequest.md)
 - [BrowseResponse](docs/BrowseResponse.md)
 - [BrowseResult](docs/BrowseResult.md)
 - [CallMethodRequest](docs/CallMethodRequest.md)
 - [CallMethodResult](docs/CallMethodResult.md)
 - [CallRequest](docs/CallRequest.md)
 - [CallResponse](docs/CallResponse.md)
 - [CancelRequest](docs/CancelRequest.md)
 - [CancelResponse](docs/CancelResponse.md)
 - [CloseSessionRequest](docs/CloseSessionRequest.md)
 - [CloseSessionResponse](docs/CloseSessionResponse.md)
 - [ConfigurationVersionDataType](docs/ConfigurationVersionDataType.md)
 - [ContentFilter](docs/ContentFilter.md)
 - [ContentFilterElement](docs/ContentFilterElement.md)
 - [ContentFilterElementResult](docs/ContentFilterElementResult.md)
 - [ContentFilterResult](docs/ContentFilterResult.md)
 - [CreateMonitoredItemsRequest](docs/CreateMonitoredItemsRequest.md)
 - [CreateMonitoredItemsResponse](docs/CreateMonitoredItemsResponse.md)
 - [CreateSessionRequest](docs/CreateSessionRequest.md)
 - [CreateSessionResponse](docs/CreateSessionResponse.md)
 - [CreateSubscriptionRequest](docs/CreateSubscriptionRequest.md)
 - [CreateSubscriptionResponse](docs/CreateSubscriptionResponse.md)
 - [DataChangeFilter](docs/DataChangeFilter.md)
 - [DataChangeNotification](docs/DataChangeNotification.md)
 - [DataChangeTrigger](docs/DataChangeTrigger.md)
 - [DataSetFieldContentMaskBits](docs/DataSetFieldContentMaskBits.md)
 - [DataSetFieldFlagsBits](docs/DataSetFieldFlagsBits.md)
 - [DataSetMetaDataType](docs/DataSetMetaDataType.md)
 - [DataSetReaderDataType](docs/DataSetReaderDataType.md)
 - [DataSetWriterDataType](docs/DataSetWriterDataType.md)
 - [DataTypeDescription](docs/DataTypeDescription.md)
 - [DataTypeSchemaHeader](docs/DataTypeSchemaHeader.md)
 - [DataValue](docs/DataValue.md)
 - [Decimal](docs/Decimal.md)
 - [DeleteMonitoredItemsRequest](docs/DeleteMonitoredItemsRequest.md)
 - [DeleteMonitoredItemsResponse](docs/DeleteMonitoredItemsResponse.md)
 - [DeleteSubscriptionsRequest](docs/DeleteSubscriptionsRequest.md)
 - [DeleteSubscriptionsResponse](docs/DeleteSubscriptionsResponse.md)
 - [DiagnosticInfo](docs/DiagnosticInfo.md)
 - [EUInformation](docs/EUInformation.md)
 - [ElementOperand](docs/ElementOperand.md)
 - [EndpointDescription](docs/EndpointDescription.md)
 - [EnumDefinition](docs/EnumDefinition.md)
 - [EnumDescription](docs/EnumDescription.md)
 - [EnumField](docs/EnumField.md)
 - [EnumValueType](docs/EnumValueType.md)
 - [EventFieldList](docs/EventFieldList.md)
 - [EventFilter](docs/EventFilter.md)
 - [EventFilterResult](docs/EventFilterResult.md)
 - [EventNotificationList](docs/EventNotificationList.md)
 - [ExtensionObject](docs/ExtensionObject.md)
 - [FieldMetaData](docs/FieldMetaData.md)
 - [FilterOperator](docs/FilterOperator.md)
 - [FindServersRequest](docs/FindServersRequest.md)
 - [FindServersResponse](docs/FindServersResponse.md)
 - [GetEndpointsRequest](docs/GetEndpointsRequest.md)
 - [GetEndpointsResponse](docs/GetEndpointsResponse.md)
 - [HistoryData](docs/HistoryData.md)
 - [HistoryEvent](docs/HistoryEvent.md)
 - [HistoryEventFieldList](docs/HistoryEventFieldList.md)
 - [HistoryModifiedData](docs/HistoryModifiedData.md)
 - [HistoryReadRequest](docs/HistoryReadRequest.md)
 - [HistoryReadResponse](docs/HistoryReadResponse.md)
 - [HistoryReadResult](docs/HistoryReadResult.md)
 - [HistoryReadValueId](docs/HistoryReadValueId.md)
 - [HistoryUpdateRequest](docs/HistoryUpdateRequest.md)
 - [HistoryUpdateResponse](docs/HistoryUpdateResponse.md)
 - [HistoryUpdateResult](docs/HistoryUpdateResult.md)
 - [HistoryUpdateType](docs/HistoryUpdateType.md)
 - [IssuedIdentityToken](docs/IssuedIdentityToken.md)
 - [JsonActionMetaDataMessage](docs/JsonActionMetaDataMessage.md)
 - [JsonActionNetworkMessage](docs/JsonActionNetworkMessage.md)
 - [JsonActionRequestMessage](docs/JsonActionRequestMessage.md)
 - [JsonActionResponderMessage](docs/JsonActionResponderMessage.md)
 - [JsonActionResponseMessage](docs/JsonActionResponseMessage.md)
 - [JsonApplicationDescriptionMessage](docs/JsonApplicationDescriptionMessage.md)
 - [JsonDataSetMessage](docs/JsonDataSetMessage.md)
 - [JsonDataSetMessageContentMaskBits](docs/JsonDataSetMessageContentMaskBits.md)
 - [JsonDataSetMetaDataMessage](docs/JsonDataSetMetaDataMessage.md)
 - [JsonDataSetReaderMessageDataType](docs/JsonDataSetReaderMessageDataType.md)
 - [JsonDataSetWriterMessageDataType](docs/JsonDataSetWriterMessageDataType.md)
 - [JsonMessageType](docs/JsonMessageType.md)
 - [JsonNetworkMessage](docs/JsonNetworkMessage.md)
 - [JsonNetworkMessageContentMaskBits](docs/JsonNetworkMessageContentMaskBits.md)
 - [JsonPubSubConnectionMessage](docs/JsonPubSubConnectionMessage.md)
 - [JsonServerEndpointsMessage](docs/JsonServerEndpointsMessage.md)
 - [JsonStatusMessage](docs/JsonStatusMessage.md)
 - [JsonWriterGroupMessageDataType](docs/JsonWriterGroupMessageDataType.md)
 - [KeyValuePair](docs/KeyValuePair.md)
 - [LiteralOperand](docs/LiteralOperand.md)
 - [LocalizedText](docs/LocalizedText.md)
 - [Matrix](docs/Matrix.md)
 - [MessageSecurityMode](docs/MessageSecurityMode.md)
 - [ModificationInfo](docs/ModificationInfo.md)
 - [ModifyMonitoredItemsRequest](docs/ModifyMonitoredItemsRequest.md)
 - [ModifyMonitoredItemsResponse](docs/ModifyMonitoredItemsResponse.md)
 - [ModifySubscriptionRequest](docs/ModifySubscriptionRequest.md)
 - [ModifySubscriptionResponse](docs/ModifySubscriptionResponse.md)
 - [MonitoredItemCreateRequest](docs/MonitoredItemCreateRequest.md)
 - [MonitoredItemCreateResult](docs/MonitoredItemCreateResult.md)
 - [MonitoredItemModifyRequest](docs/MonitoredItemModifyRequest.md)
 - [MonitoredItemModifyResult](docs/MonitoredItemModifyResult.md)
 - [MonitoredItemNotification](docs/MonitoredItemNotification.md)
 - [MonitoringMode](docs/MonitoringMode.md)
 - [MonitoringParameters](docs/MonitoringParameters.md)
 - [NetworkAddressDataType](docs/NetworkAddressDataType.md)
 - [NodeClass](docs/NodeClass.md)
 - [NotificationMessage](docs/NotificationMessage.md)
 - [PerformUpdateType](docs/PerformUpdateType.md)
 - [PermissionTypeBits](docs/PermissionTypeBits.md)
 - [PubSubConfiguration2DataType](docs/PubSubConfiguration2DataType.md)
 - [PubSubConfigurationDataType](docs/PubSubConfigurationDataType.md)
 - [PubSubConnectionDataType](docs/PubSubConnectionDataType.md)
 - [PubSubGroupDataType](docs/PubSubGroupDataType.md)
 - [PubSubKeyPushTargetDataType](docs/PubSubKeyPushTargetDataType.md)
 - [PubSubState](docs/PubSubState.md)
 - [PublishRequest](docs/PublishRequest.md)
 - [PublishResponse](docs/PublishResponse.md)
 - [PublishedDataSetDataType](docs/PublishedDataSetDataType.md)
 - [Range](docs/Range.md)
 - [ReadAnnotationDataDetails](docs/ReadAnnotationDataDetails.md)
 - [ReadAtTimeDetails](docs/ReadAtTimeDetails.md)
 - [ReadEventDetails](docs/ReadEventDetails.md)
 - [ReadEventDetails2](docs/ReadEventDetails2.md)
 - [ReadProcessedDetails](docs/ReadProcessedDetails.md)
 - [ReadRawModifiedDetails](docs/ReadRawModifiedDetails.md)
 - [ReadRequest](docs/ReadRequest.md)
 - [ReadResponse](docs/ReadResponse.md)
 - [ReadValueId](docs/ReadValueId.md)
 - [ReaderGroupDataType](docs/ReaderGroupDataType.md)
 - [ReferenceDescription](docs/ReferenceDescription.md)
 - [RegisterNodesRequest](docs/RegisterNodesRequest.md)
 - [RegisterNodesResponse](docs/RegisterNodesResponse.md)
 - [RelativePath](docs/RelativePath.md)
 - [RelativePathElement](docs/RelativePathElement.md)
 - [RepublishRequest](docs/RepublishRequest.md)
 - [RepublishResponse](docs/RepublishResponse.md)
 - [RequestHeader](docs/RequestHeader.md)
 - [ResponseHeader](docs/ResponseHeader.md)
 - [RolePermissionType](docs/RolePermissionType.md)
 - [SecurityGroupDataType](docs/SecurityGroupDataType.md)
 - [SetMonitoringModeRequest](docs/SetMonitoringModeRequest.md)
 - [SetMonitoringModeResponse](docs/SetMonitoringModeResponse.md)
 - [SetPublishingModeRequest](docs/SetPublishingModeRequest.md)
 - [SetPublishingModeResponse](docs/SetPublishingModeResponse.md)
 - [SetTriggeringRequest](docs/SetTriggeringRequest.md)
 - [SetTriggeringResponse](docs/SetTriggeringResponse.md)
 - [SignatureData](docs/SignatureData.md)
 - [SignedSoftwareCertificate](docs/SignedSoftwareCertificate.md)
 - [SimpleAttributeOperand](docs/SimpleAttributeOperand.md)
 - [SimpleTypeDescription](docs/SimpleTypeDescription.md)
 - [StandaloneSubscribedDataSetDataType](docs/StandaloneSubscribedDataSetDataType.md)
 - [StatusChangeNotification](docs/StatusChangeNotification.md)
 - [StatusCode](docs/StatusCode.md)
 - [StructureDefinition](docs/StructureDefinition.md)
 - [StructureDescription](docs/StructureDescription.md)
 - [StructureField](docs/StructureField.md)
 - [StructureType](docs/StructureType.md)
 - [SubscriptionAcknowledgement](docs/SubscriptionAcknowledgement.md)
 - [TimestampsToReturn](docs/TimestampsToReturn.md)
 - [TransferResult](docs/TransferResult.md)
 - [TransferSubscriptionsRequest](docs/TransferSubscriptionsRequest.md)
 - [TransferSubscriptionsResponse](docs/TransferSubscriptionsResponse.md)
 - [TranslateBrowsePathsToNodeIdsRequest](docs/TranslateBrowsePathsToNodeIdsRequest.md)
 - [TranslateBrowsePathsToNodeIdsResponse](docs/TranslateBrowsePathsToNodeIdsResponse.md)
 - [UnregisterNodesRequest](docs/UnregisterNodesRequest.md)
 - [UnregisterNodesResponse](docs/UnregisterNodesResponse.md)
 - [UpdateDataDetails](docs/UpdateDataDetails.md)
 - [UpdateEventDetails](docs/UpdateEventDetails.md)
 - [UpdateStructureDataDetails](docs/UpdateStructureDataDetails.md)
 - [UserIdentityToken](docs/UserIdentityToken.md)
 - [UserNameIdentityToken](docs/UserNameIdentityToken.md)
 - [UserTokenPolicy](docs/UserTokenPolicy.md)
 - [UserTokenType](docs/UserTokenType.md)
 - [Variant](docs/Variant.md)
 - [ViewDescription](docs/ViewDescription.md)
 - [WriteRequest](docs/WriteRequest.md)
 - [WriteResponse](docs/WriteResponse.md)
 - [WriteValue](docs/WriteValue.md)
 - [WriterGroupDataType](docs/WriterGroupDataType.md)
 - [X509IdentityToken](docs/X509IdentityToken.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

office@opcfoundation.org


