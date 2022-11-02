# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import WebPubSubManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    Operations,
    UsagesOperations,
    WebPubSubCustomCertificatesOperations,
    WebPubSubCustomDomainsOperations,
    WebPubSubHubsOperations,
    WebPubSubOperations,
    WebPubSubPrivateEndpointConnectionsOperations,
    WebPubSubPrivateLinkResourcesOperations,
    WebPubSubSharedPrivateLinkResourcesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class WebPubSubManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """REST API for Azure WebPubSub Service.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.webpubsub.operations.Operations
    :ivar web_pub_sub: WebPubSubOperations operations
    :vartype web_pub_sub: azure.mgmt.webpubsub.operations.WebPubSubOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.webpubsub.operations.UsagesOperations
    :ivar web_pub_sub_custom_certificates: WebPubSubCustomCertificatesOperations operations
    :vartype web_pub_sub_custom_certificates:
     azure.mgmt.webpubsub.operations.WebPubSubCustomCertificatesOperations
    :ivar web_pub_sub_custom_domains: WebPubSubCustomDomainsOperations operations
    :vartype web_pub_sub_custom_domains:
     azure.mgmt.webpubsub.operations.WebPubSubCustomDomainsOperations
    :ivar web_pub_sub_hubs: WebPubSubHubsOperations operations
    :vartype web_pub_sub_hubs: azure.mgmt.webpubsub.operations.WebPubSubHubsOperations
    :ivar web_pub_sub_private_endpoint_connections: WebPubSubPrivateEndpointConnectionsOperations
     operations
    :vartype web_pub_sub_private_endpoint_connections:
     azure.mgmt.webpubsub.operations.WebPubSubPrivateEndpointConnectionsOperations
    :ivar web_pub_sub_private_link_resources: WebPubSubPrivateLinkResourcesOperations operations
    :vartype web_pub_sub_private_link_resources:
     azure.mgmt.webpubsub.operations.WebPubSubPrivateLinkResourcesOperations
    :ivar web_pub_sub_shared_private_link_resources: WebPubSubSharedPrivateLinkResourcesOperations
     operations
    :vartype web_pub_sub_shared_private_link_resources:
     azure.mgmt.webpubsub.operations.WebPubSubSharedPrivateLinkResourcesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-08-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = WebPubSubManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub = WebPubSubOperations(self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_custom_certificates = WebPubSubCustomCertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_custom_domains = WebPubSubCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_hubs = WebPubSubHubsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_private_endpoint_connections = WebPubSubPrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_private_link_resources = WebPubSubPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_shared_private_link_resources = WebPubSubSharedPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> WebPubSubManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
