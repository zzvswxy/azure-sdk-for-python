# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

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
from ...operations._operations import build_changes_get_request, build_changes_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ChangesOperations:
    """ChangesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.changes.v2022_05_01.models
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
        resource_group_name: str,
        resource_provider_namespace: str,
        resource_type: str,
        resource_name: str,
        top: Optional[int] = 100,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ChangeResourceListResult"]:
        """Obtains a list of change resources from the past 14 days for the target resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_provider_namespace: The name of the resource provider namespace.
        :type resource_provider_namespace: str
        :param resource_type: The name of the resource type.
        :type resource_type: str
        :param resource_name: The name of the resource.
        :type resource_name: str
        :param top: (Optional) Set the maximum number of results per response. Default value is 100.
        :type top: long
        :param skip_token: (Optional) The page-continuation token. Default value is None.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ChangeResourceListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.changes.v2022_05_01.models.ChangeResourceListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-05-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ChangeResourceListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_changes_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    api_version=api_version,
                    top=top,
                    skip_token=skip_token,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_changes_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ChangeResourceListResult", pipeline_response)
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
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Resources/changes"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        resource_provider_namespace: str,
        resource_type: str,
        resource_name: str,
        change_resource_id: str,
        **kwargs: Any
    ) -> "_models.ChangeResourceResult":
        """Obtains the specified change resource for the target resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_provider_namespace: The name of the resource provider namespace.
        :type resource_provider_namespace: str
        :param resource_type: The name of the resource type.
        :type resource_type: str
        :param resource_name: The name of the resource.
        :type resource_name: str
        :param change_resource_id: The ID of the change resource.
        :type change_resource_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ChangeResourceResult, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.changes.v2022_05_01.models.ChangeResourceResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ChangeResourceResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-05-01")  # type: str

        
        request = build_changes_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_provider_namespace=resource_provider_namespace,
            resource_type=resource_type,
            resource_name=resource_name,
            change_resource_id=change_resource_id,
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

        deserialized = self._deserialize('ChangeResourceResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Resources/changes/{changeResourceId}"}  # type: ignore

