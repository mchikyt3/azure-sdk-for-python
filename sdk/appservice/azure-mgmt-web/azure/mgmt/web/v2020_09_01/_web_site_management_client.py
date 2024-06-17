# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import WebSiteManagementClientConfiguration
from .operations import (
    AppServiceCertificateOrdersOperations,
    AppServiceEnvironmentsOperations,
    AppServicePlansOperations,
    CertificateRegistrationProviderOperations,
    CertificatesOperations,
    DeletedWebAppsOperations,
    DiagnosticsOperations,
    DomainRegistrationProviderOperations,
    DomainsOperations,
    ProviderOperations,
    RecommendationsOperations,
    ResourceHealthMetadataOperations,
    StaticSitesOperations,
    TopLevelDomainsOperations,
    WebAppsOperations,
    WebSiteManagementClientOperationsMixin,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class WebSiteManagementClient(
    WebSiteManagementClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """WebSite Management Client.

    :ivar app_service_certificate_orders: AppServiceCertificateOrdersOperations operations
    :vartype app_service_certificate_orders:
     azure.mgmt.web.v2020_09_01.operations.AppServiceCertificateOrdersOperations
    :ivar certificate_registration_provider: CertificateRegistrationProviderOperations operations
    :vartype certificate_registration_provider:
     azure.mgmt.web.v2020_09_01.operations.CertificateRegistrationProviderOperations
    :ivar domains: DomainsOperations operations
    :vartype domains: azure.mgmt.web.v2020_09_01.operations.DomainsOperations
    :ivar top_level_domains: TopLevelDomainsOperations operations
    :vartype top_level_domains: azure.mgmt.web.v2020_09_01.operations.TopLevelDomainsOperations
    :ivar domain_registration_provider: DomainRegistrationProviderOperations operations
    :vartype domain_registration_provider:
     azure.mgmt.web.v2020_09_01.operations.DomainRegistrationProviderOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.web.v2020_09_01.operations.CertificatesOperations
    :ivar deleted_web_apps: DeletedWebAppsOperations operations
    :vartype deleted_web_apps: azure.mgmt.web.v2020_09_01.operations.DeletedWebAppsOperations
    :ivar diagnostics: DiagnosticsOperations operations
    :vartype diagnostics: azure.mgmt.web.v2020_09_01.operations.DiagnosticsOperations
    :ivar provider: ProviderOperations operations
    :vartype provider: azure.mgmt.web.v2020_09_01.operations.ProviderOperations
    :ivar recommendations: RecommendationsOperations operations
    :vartype recommendations: azure.mgmt.web.v2020_09_01.operations.RecommendationsOperations
    :ivar web_apps: WebAppsOperations operations
    :vartype web_apps: azure.mgmt.web.v2020_09_01.operations.WebAppsOperations
    :ivar static_sites: StaticSitesOperations operations
    :vartype static_sites: azure.mgmt.web.v2020_09_01.operations.StaticSitesOperations
    :ivar app_service_environments: AppServiceEnvironmentsOperations operations
    :vartype app_service_environments:
     azure.mgmt.web.v2020_09_01.operations.AppServiceEnvironmentsOperations
    :ivar app_service_plans: AppServicePlansOperations operations
    :vartype app_service_plans: azure.mgmt.web.v2020_09_01.operations.AppServicePlansOperations
    :ivar resource_health_metadata: ResourceHealthMetadataOperations operations
    :vartype resource_health_metadata:
     azure.mgmt.web.v2020_09_01.operations.ResourceHealthMetadataOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g.
     00000000-0000-0000-0000-000000000000). Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2020-09-01". Note that overriding this
     default value may result in unsupported behavior.
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
        self._config = WebSiteManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.app_service_certificate_orders = AppServiceCertificateOrdersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.certificate_registration_provider = CertificateRegistrationProviderOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.domains = DomainsOperations(self._client, self._config, self._serialize, self._deserialize, "2020-09-01")
        self.top_level_domains = TopLevelDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.domain_registration_provider = DomainRegistrationProviderOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.deleted_web_apps = DeletedWebAppsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.diagnostics = DiagnosticsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.provider = ProviderOperations(self._client, self._config, self._serialize, self._deserialize, "2020-09-01")
        self.recommendations = RecommendationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.web_apps = WebAppsOperations(self._client, self._config, self._serialize, self._deserialize, "2020-09-01")
        self.static_sites = StaticSitesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.app_service_environments = AppServiceEnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.app_service_plans = AppServicePlansOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )
        self.resource_health_metadata = ResourceHealthMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-09-01"
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
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
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "WebSiteManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
