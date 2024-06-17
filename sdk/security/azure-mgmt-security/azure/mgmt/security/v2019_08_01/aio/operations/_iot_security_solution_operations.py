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
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._iot_security_solution_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_by_subscription_request,
    build_update_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class IotSecuritySolutionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2019_08_01.aio.SecurityCenter`'s
        :attr:`iot_security_solution` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list_by_subscription(
        self, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.IoTSecuritySolutionModel"]:
        """Use this method to get the list of IoT Security solutions by subscription.

        :param filter: Filter the IoT Security solution with OData syntax. Supports filtering by
         iotHubs. Default value is None.
        :type filter: str
        :return: An iterator like instance of either IoTSecuritySolutionModel or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-08-01"))
        cls: ClsType[_models.IoTSecuritySolutionsList] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("IoTSecuritySolutionsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.IoTSecuritySolutionModel"]:
        """Use this method to get the list IoT Security solutions organized by resource group.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param filter: Filter the IoT Security solution with OData syntax. Supports filtering by
         iotHubs. Default value is None.
        :type filter: str
        :return: An iterator like instance of either IoTSecuritySolutionModel or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-08-01"))
        cls: ClsType[_models.IoTSecuritySolutionsList] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("IoTSecuritySolutionsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, solution_name: str, **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """User this method to get details of a specific IoT Security solution based on solution name.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-08-01"))
        cls: ClsType[_models.IoTSecuritySolutionModel] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            solution_name=solution_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("IoTSecuritySolutionModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        solution_name: str,
        iot_security_solution_data: _models.IoTSecuritySolutionModel,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """Use this method to create or update yours IoT Security solution.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :param iot_security_solution_data: The security solution data. Required.
        :type iot_security_solution_data:
         ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        solution_name: str,
        iot_security_solution_data: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """Use this method to create or update yours IoT Security solution.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :param iot_security_solution_data: The security solution data. Required.
        :type iot_security_solution_data: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        solution_name: str,
        iot_security_solution_data: Union[_models.IoTSecuritySolutionModel, IO[bytes]],
        **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """Use this method to create or update yours IoT Security solution.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :param iot_security_solution_data: The security solution data. Is either a
         IoTSecuritySolutionModel type or a IO[bytes] type. Required.
        :type iot_security_solution_data:
         ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel or IO[bytes]
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-08-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.IoTSecuritySolutionModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(iot_security_solution_data, (IOBase, bytes)):
            _content = iot_security_solution_data
        else:
            _json = self._serialize.body(iot_security_solution_data, "IoTSecuritySolutionModel")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            solution_name=solution_name,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("IoTSecuritySolutionModel", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("IoTSecuritySolutionModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        solution_name: str,
        update_iot_security_solution_data: _models.UpdateIotSecuritySolutionData,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """Use this method to update existing IoT Security solution tags or user defined resources. To
        update other fields use the CreateOrUpdate method.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :param update_iot_security_solution_data: The security solution data. Required.
        :type update_iot_security_solution_data:
         ~azure.mgmt.security.v2019_08_01.models.UpdateIotSecuritySolutionData
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        solution_name: str,
        update_iot_security_solution_data: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """Use this method to update existing IoT Security solution tags or user defined resources. To
        update other fields use the CreateOrUpdate method.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :param update_iot_security_solution_data: The security solution data. Required.
        :type update_iot_security_solution_data: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        solution_name: str,
        update_iot_security_solution_data: Union[_models.UpdateIotSecuritySolutionData, IO[bytes]],
        **kwargs: Any
    ) -> _models.IoTSecuritySolutionModel:
        """Use this method to update existing IoT Security solution tags or user defined resources. To
        update other fields use the CreateOrUpdate method.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
        :param update_iot_security_solution_data: The security solution data. Is either a
         UpdateIotSecuritySolutionData type or a IO[bytes] type. Required.
        :type update_iot_security_solution_data:
         ~azure.mgmt.security.v2019_08_01.models.UpdateIotSecuritySolutionData or IO[bytes]
        :return: IoTSecuritySolutionModel or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_08_01.models.IoTSecuritySolutionModel
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-08-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.IoTSecuritySolutionModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(update_iot_security_solution_data, (IOBase, bytes)):
            _content = update_iot_security_solution_data
        else:
            _json = self._serialize.body(update_iot_security_solution_data, "UpdateIotSecuritySolutionData")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            solution_name=solution_name,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("IoTSecuritySolutionModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, solution_name: str, **kwargs: Any
    ) -> None:
        """Use this method to delete yours IoT Security solution.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param solution_name: The name of the IoT Security solution. Required.
        :type solution_name: str
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-08-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            solution_name=solution_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
