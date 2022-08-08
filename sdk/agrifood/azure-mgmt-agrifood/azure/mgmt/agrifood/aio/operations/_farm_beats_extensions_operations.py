# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, List, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._farm_beats_extensions_operations import build_get_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FarmBeatsExtensionsOperations:
    """FarmBeatsExtensionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.agrifood.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        farm_beats_extension_ids: Optional[List[str]] = None,
        farm_beats_extension_names: Optional[List[str]] = None,
        extension_categories: Optional[List[str]] = None,
        publisher_ids: Optional[List[str]] = None,
        max_page_size: Optional[int] = 50,
        **kwargs: Any
    ) -> AsyncIterable["_models.FarmBeatsExtensionListResponse"]:
        """Get list of farmBeats extension.

        :param farm_beats_extension_ids: FarmBeatsExtension ids. Default value is None.
        :type farm_beats_extension_ids: list[str]
        :param farm_beats_extension_names: FarmBeats extension names. Default value is None.
        :type farm_beats_extension_names: list[str]
        :param extension_categories: Extension categories. Default value is None.
        :type extension_categories: list[str]
        :param publisher_ids: Publisher ids. Default value is None.
        :type publisher_ids: list[str]
        :param max_page_size: Maximum number of items needed (inclusive).
         Minimum = 10, Maximum = 1000, Default value = 50. Default value is 50.
        :type max_page_size: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FarmBeatsExtensionListResponse or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.agrifood.models.FarmBeatsExtensionListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-03-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FarmBeatsExtensionListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    api_version=api_version,
                    farm_beats_extension_ids=farm_beats_extension_ids,
                    farm_beats_extension_names=farm_beats_extension_names,
                    extension_categories=extension_categories,
                    publisher_ids=publisher_ids,
                    max_page_size=max_page_size,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    api_version=api_version,
                    farm_beats_extension_ids=farm_beats_extension_ids,
                    farm_beats_extension_names=farm_beats_extension_names,
                    extension_categories=extension_categories,
                    publisher_ids=publisher_ids,
                    max_page_size=max_page_size,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FarmBeatsExtensionListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/providers/Microsoft.AgFoodPlatform/farmBeatsExtensionDefinitions"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        farm_beats_extension_id: str,
        **kwargs: Any
    ) -> "_models.FarmBeatsExtension":
        """Get farmBeats extension.

        :param farm_beats_extension_id: farmBeatsExtensionId to be queried.
        :type farm_beats_extension_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FarmBeatsExtension, or the result of cls(response)
        :rtype: ~azure.mgmt.agrifood.models.FarmBeatsExtension
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FarmBeatsExtension"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-03-01")  # type: str

        
        request = build_get_request(
            farm_beats_extension_id=farm_beats_extension_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FarmBeatsExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/providers/Microsoft.AgFoodPlatform/farmBeatsExtensionDefinitions/{farmBeatsExtensionId}"}  # type: ignore

