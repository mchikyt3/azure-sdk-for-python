# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._run_notebook_operations import (
    build_cancel_run_request,
    build_create_run_request,
    build_get_snapshot_request,
    build_get_status_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class RunNotebookOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.synapse.artifacts.aio.ArtifactsClient`'s
        :attr:`run_notebook` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_run_initial(
        self, run_id: str, run_notebook_request: Union[_models.RunNotebookRequest, IO[bytes]], **kwargs: Any
    ) -> _models.RunNotebookResponse:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01-preview"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.RunNotebookResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(run_notebook_request, (IOBase, bytes)):
            _content = run_notebook_request
        else:
            _json = self._serialize.body(run_notebook_request, "RunNotebookRequest")

        _request = build_create_run_request(
            run_id=run_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        deserialized = self._deserialize("RunNotebookResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_run(
        self,
        run_id: str,
        run_notebook_request: _models.RunNotebookRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.RunNotebookResponse]:
        """Run notebook.

        :param run_id: Notebook run id. Required.
        :type run_id: str
        :param run_notebook_request: Run notebook request payload. Required.
        :type run_notebook_request: ~azure.synapse.artifacts.models.RunNotebookRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either RunNotebookResponse or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.RunNotebookResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_run(
        self, run_id: str, run_notebook_request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.RunNotebookResponse]:
        """Run notebook.

        :param run_id: Notebook run id. Required.
        :type run_id: str
        :param run_notebook_request: Run notebook request payload. Required.
        :type run_notebook_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either RunNotebookResponse or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.RunNotebookResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_run(
        self, run_id: str, run_notebook_request: Union[_models.RunNotebookRequest, IO[bytes]], **kwargs: Any
    ) -> AsyncLROPoller[_models.RunNotebookResponse]:
        """Run notebook.

        :param run_id: Notebook run id. Required.
        :type run_id: str
        :param run_notebook_request: Run notebook request payload. Is either a RunNotebookRequest type
         or a IO[bytes] type. Required.
        :type run_notebook_request: ~azure.synapse.artifacts.models.RunNotebookRequest or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either RunNotebookResponse or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.RunNotebookResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01-preview"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.RunNotebookResponse] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_run_initial(
                run_id=run_id,
                run_notebook_request=run_notebook_request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

            deserialized = self._deserialize("RunNotebookResponse", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.RunNotebookResponse].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.RunNotebookResponse](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def get_status(self, run_id: str, **kwargs: Any) -> _models.RunNotebookResponse:
        """Get RunNotebook Status for run id.

        :param run_id: Notebook run id. Required.
        :type run_id: str
        :return: RunNotebookResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.RunNotebookResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01-preview"))
        cls: ClsType[_models.RunNotebookResponse] = kwargs.pop("cls", None)

        _request = build_get_status_request(
            run_id=run_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("RunNotebookResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def cancel_run(self, run_id: str, **kwargs: Any) -> _models.RunNotebookResponse:
        """Cancel notebook run.

        :param run_id: Notebook run id. Required.
        :type run_id: str
        :return: RunNotebookResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.RunNotebookResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            304: ResourceNotModifiedError,
            409: lambda response: ResourceExistsError(
                response=response, model=self._deserialize(_models.RunNotebookResponse, response)
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01-preview"))
        cls: ClsType[_models.RunNotebookResponse] = kwargs.pop("cls", None)

        _request = build_cancel_run_request(
            run_id=run_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)  # type: ignore
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("RunNotebookResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get_snapshot(self, run_id: str, **kwargs: Any) -> _models.RunNotebookSnapshotResponse:
        """Get RunNotebook Snapshot for run id.

        :param run_id: Notebook run id. Required.
        :type run_id: str
        :return: RunNotebookSnapshotResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.RunNotebookSnapshotResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01-preview"))
        cls: ClsType[_models.RunNotebookSnapshotResponse] = kwargs.pop("cls", None)

        _request = build_get_snapshot_request(
            run_id=run_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("RunNotebookSnapshotResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
