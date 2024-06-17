# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_group_name: str,
    account_name: str,
    management_policy_name: Union[str, _models.ManagementPolicyName],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "managementPolicyName": _SERIALIZER.url("management_policy_name", management_policy_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    account_name: str,
    management_policy_name: Union[str, _models.ManagementPolicyName],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "managementPolicyName": _SERIALIZER.url("management_policy_name", management_policy_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    account_name: str,
    management_policy_name: Union[str, _models.ManagementPolicyName],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01-preview"))
    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "managementPolicyName": _SERIALIZER.url("management_policy_name", management_policy_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


class ManagementPoliciesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2020_08_01_preview.StorageManagementClient`'s
        :attr:`management_policies` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        account_name: str,
        management_policy_name: Union[str, _models.ManagementPolicyName],
        **kwargs: Any
    ) -> _models.ManagementPolicy:
        """Gets the managementpolicy associated with the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param management_policy_name: The name of the Storage Account Management Policy. It should
         always be 'default'. "default" Required.
        :type management_policy_name: str or
         ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicyName
        :return: ManagementPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2020-08-01-preview")
        )
        cls: ClsType[_models.ManagementPolicy] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            management_policy_name=management_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ManagementPolicy", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        account_name: str,
        management_policy_name: Union[str, _models.ManagementPolicyName],
        properties: _models.ManagementPolicy,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagementPolicy:
        """Sets the managementpolicy to the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param management_policy_name: The name of the Storage Account Management Policy. It should
         always be 'default'. "default" Required.
        :type management_policy_name: str or
         ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicyName
        :param properties: The ManagementPolicy set to a storage account. Required.
        :type properties: ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagementPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        account_name: str,
        management_policy_name: Union[str, _models.ManagementPolicyName],
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagementPolicy:
        """Sets the managementpolicy to the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param management_policy_name: The name of the Storage Account Management Policy. It should
         always be 'default'. "default" Required.
        :type management_policy_name: str or
         ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicyName
        :param properties: The ManagementPolicy set to a storage account. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagementPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        account_name: str,
        management_policy_name: Union[str, _models.ManagementPolicyName],
        properties: Union[_models.ManagementPolicy, IO[bytes]],
        **kwargs: Any
    ) -> _models.ManagementPolicy:
        """Sets the managementpolicy to the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param management_policy_name: The name of the Storage Account Management Policy. It should
         always be 'default'. "default" Required.
        :type management_policy_name: str or
         ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicyName
        :param properties: The ManagementPolicy set to a storage account. Is either a ManagementPolicy
         type or a IO[bytes] type. Required.
        :type properties: ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicy or IO[bytes]
        :return: ManagementPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2020-08-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ManagementPolicy] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "ManagementPolicy")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            management_policy_name=management_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ManagementPolicy", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        account_name: str,
        management_policy_name: Union[str, _models.ManagementPolicyName],
        **kwargs: Any
    ) -> None:
        """Deletes the managementpolicy associated with the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param management_policy_name: The name of the Storage Account Management Policy. It should
         always be 'default'. "default" Required.
        :type management_policy_name: str or
         ~azure.mgmt.storage.v2020_08_01_preview.models.ManagementPolicyName
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2020-08-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            management_policy_name=management_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
