# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, Type, TypeVar, Union, cast
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import WebSiteManagementClientMixinABC, _convert_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str,
    name: str,
    workflow_name: str,
    trigger_name: str,
    subscription_id: str,
    *,
    top: Optional[int] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostruntime/runtime/webhooks/workflow/api/management/workflows/{workflowName}/triggers/{triggerName}/histories",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name",
            resource_group_name,
            "str",
            max_length=90,
            min_length=1,
            pattern=r"^[-\w\._\(\)]+[^\.]$",
        ),
        "name": _SERIALIZER.url("name", name, "str"),
        "workflowName": _SERIALIZER.url("workflow_name", workflow_name, "str"),
        "triggerName": _SERIALIZER.url("trigger_name", trigger_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    name: str,
    workflow_name: str,
    trigger_name: str,
    history_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostruntime/runtime/webhooks/workflow/api/management/workflows/{workflowName}/triggers/{triggerName}/histories/{historyName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name",
            resource_group_name,
            "str",
            max_length=90,
            min_length=1,
            pattern=r"^[-\w\._\(\)]+[^\.]$",
        ),
        "name": _SERIALIZER.url("name", name, "str"),
        "workflowName": _SERIALIZER.url("workflow_name", workflow_name, "str"),
        "triggerName": _SERIALIZER.url("trigger_name", trigger_name, "str"),
        "historyName": _SERIALIZER.url("history_name", history_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_resubmit_request(
    resource_group_name: str,
    name: str,
    workflow_name: str,
    trigger_name: str,
    history_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostruntime/runtime/webhooks/workflow/api/management/workflows/{workflowName}/triggers/{triggerName}/histories/{historyName}/resubmit",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name",
            resource_group_name,
            "str",
            max_length=90,
            min_length=1,
            pattern=r"^[-\w\._\(\)]+[^\.]$",
        ),
        "name": _SERIALIZER.url("name", name, "str"),
        "workflowName": _SERIALIZER.url("workflow_name", workflow_name, "str"),
        "triggerName": _SERIALIZER.url("trigger_name", trigger_name, "str"),
        "historyName": _SERIALIZER.url("history_name", history_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class WorkflowTriggerHistoriesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.web.v2022_09_01.WebSiteManagementClient`'s
        :attr:`workflow_trigger_histories` attribute.
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
    def list(
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        trigger_name: str,
        top: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.WorkflowTriggerHistory"]:
        """Gets a list of workflow trigger histories.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name. Required.
        :type trigger_name: str
        :param top: The number of items to be included in the result. Default value is None.
        :type top: int
        :param filter: The filter to apply on the operation. Options for filters include: Status,
         StartTime, and ClientTrackingId. Default value is None.
        :type filter: str
        :return: An iterator like instance of either WorkflowTriggerHistory or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.web.v2022_09_01.models.WorkflowTriggerHistory]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-09-01"))
        cls: ClsType[_models.WorkflowTriggerHistoryListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    resource_group_name=resource_group_name,
                    name=name,
                    workflow_name=workflow_name,
                    trigger_name=trigger_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    filter=filter,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("WorkflowTriggerHistoryListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        trigger_name: str,
        history_name: str,
        **kwargs: Any
    ) -> _models.WorkflowTriggerHistory:
        """Gets a workflow trigger history.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name. Required.
        :type trigger_name: str
        :param history_name: The workflow trigger history name. Corresponds to the run name for
         triggers that resulted in a run. Required.
        :type history_name: str
        :return: WorkflowTriggerHistory or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2022_09_01.models.WorkflowTriggerHistory
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-09-01"))
        cls: ClsType[_models.WorkflowTriggerHistory] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            name=name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            history_name=history_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WorkflowTriggerHistory", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def _resubmit_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        trigger_name: str,
        history_name: str,
        **kwargs: Any
    ) -> None:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-09-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_resubmit_request(
            resource_group_name=resource_group_name,
            name=name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            history_name=history_name,
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

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def begin_resubmit(
        self,
        resource_group_name: str,
        name: str,
        workflow_name: str,
        trigger_name: str,
        history_name: str,
        **kwargs: Any
    ) -> LROPoller[None]:
        """Resubmits a workflow run based on the trigger history.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param name: Site name. Required.
        :type name: str
        :param workflow_name: The workflow name. Required.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name. Required.
        :type trigger_name: str
        :param history_name: The workflow trigger history name. Corresponds to the run name for
         triggers that resulted in a run. Required.
        :type history_name: str
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-09-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._resubmit_initial(  # type: ignore
                resource_group_name=resource_group_name,
                name=name,
                workflow_name=workflow_name,
                trigger_name=trigger_name,
                history_name=history_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: PollingMethod = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
