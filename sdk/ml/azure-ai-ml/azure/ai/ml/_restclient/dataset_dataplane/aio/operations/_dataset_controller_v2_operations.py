# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

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
from ...operations._dataset_controller_v2_operations import build_delete_all_datasets_request, build_get_all_dataset_definitions_request, build_get_all_dataset_versions_request, build_get_dataset_by_name_request, build_get_dataset_definition_request, build_list_request, build_register_request, build_unregister_dataset_request, build_update_dataset_request, build_update_definition_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DatasetControllerV2Operations:
    """DatasetControllerV2Operations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
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

    @distributed_trace_async
    async def get_dataset_definition(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_id: str,
        version: str,
        **kwargs: Any
    ) -> "_models.DatasetDefinition":
        """Get a specific dataset definition.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :param version:
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.DatasetDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_dataset_definition_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_id=dataset_id,
            version=version,
            template_url=self.get_dataset_definition.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DatasetDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dataset_definition.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}/definitions/{version}'}  # type: ignore


    @distributed_trace
    def get_all_dataset_definitions(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_id: str,
        continuation_token_parameter: Optional[str] = None,
        page_size: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PaginatedDatasetDefinitionList"]:
        """Get all dataset definitions for a given dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :param continuation_token_parameter:
        :type continuation_token_parameter: str
        :param page_size:
        :type page_size: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedDatasetDefinitionList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedDatasetDefinitionList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedDatasetDefinitionList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_all_dataset_definitions_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    dataset_id=dataset_id,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    template_url=self.get_all_dataset_definitions.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_get_all_dataset_definitions_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    dataset_id=dataset_id,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedDatasetDefinitionList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    get_all_dataset_definitions.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}/definitions'}  # type: ignore

    @distributed_trace_async
    async def update_definition(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_id: str,
        register_as_pending: Optional[bool] = False,
        force_update: Optional[bool] = False,
        dataset_type: Optional[str] = None,
        user_version_id: Optional[str] = None,
        body: Optional["_models.DatasetDefinition"] = None,
        **kwargs: Any
    ) -> "_models.Dataset":
        """Update a dataset definition.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :param register_as_pending:
        :type register_as_pending: bool
        :param force_update:
        :type force_update: bool
        :param dataset_type:
        :type dataset_type: str
        :param user_version_id:
        :type user_version_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.DatasetDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dataset, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Dataset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Dataset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'DatasetDefinition')
        else:
            _json = None

        request = build_update_definition_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_id=dataset_id,
            content_type=content_type,
            json=_json,
            register_as_pending=register_as_pending,
            force_update=force_update,
            dataset_type=dataset_type,
            user_version_id=user_version_id,
            template_url=self.update_definition.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Dataset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_definition.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}/definitions'}  # type: ignore


    @distributed_trace
    def get_all_dataset_versions(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_id: str,
        continuation_token_parameter: Optional[str] = None,
        page_size: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PaginatedStringList"]:
        """Get all dataset versions for a given dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :param continuation_token_parameter:
        :type continuation_token_parameter: str
        :param page_size:
        :type page_size: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedStringList or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedStringList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedStringList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_all_dataset_versions_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    dataset_id=dataset_id,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    template_url=self.get_all_dataset_versions.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_get_all_dataset_versions_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    dataset_id=dataset_id,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedStringList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    get_all_dataset_versions.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}/versions'}  # type: ignore

    @distributed_trace_async
    async def get_dataset_by_name(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_name: str,
        version_id: Optional[str] = None,
        include_latest_definition: Optional[bool] = True,
        **kwargs: Any
    ) -> "_models.Dataset":
        """Get a dataset for a given dataset name.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_name:
        :type dataset_name: str
        :param version_id:
        :type version_id: str
        :param include_latest_definition:
        :type include_latest_definition: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dataset, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Dataset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Dataset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_dataset_by_name_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_name=dataset_name,
            version_id=version_id,
            include_latest_definition=include_latest_definition,
            template_url=self.get_dataset_by_name.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Dataset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dataset_by_name.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/query/name={datasetName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_names: Optional[List[str]] = None,
        search_text: Optional[str] = None,
        include_invisible: Optional[bool] = False,
        status: Optional[str] = None,
        continuation_token_parameter: Optional[str] = None,
        page_size: Optional[int] = None,
        include_latest_definition: Optional[bool] = False,
        order_by: Optional[str] = None,
        order_by_asc: Optional[bool] = False,
        dataset_types: Optional[List[str]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PaginatedDatasetList"]:
        """Get a list of datasets.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_names:
        :type dataset_names: list[str]
        :param search_text:
        :type search_text: str
        :param include_invisible:
        :type include_invisible: bool
        :param status:
        :type status: str
        :param continuation_token_parameter:
        :type continuation_token_parameter: str
        :param page_size:
        :type page_size: int
        :param include_latest_definition:
        :type include_latest_definition: bool
        :param order_by:
        :type order_by: str
        :param order_by_asc:
        :type order_by_asc: bool
        :param dataset_types:
        :type dataset_types: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedDatasetList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedDatasetList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedDatasetList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    dataset_names=dataset_names,
                    search_text=search_text,
                    include_invisible=include_invisible,
                    status=status,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    include_latest_definition=include_latest_definition,
                    order_by=order_by,
                    order_by_asc=order_by_asc,
                    dataset_types=dataset_types,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    dataset_names=dataset_names,
                    search_text=search_text,
                    include_invisible=include_invisible,
                    status=status,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    include_latest_definition=include_latest_definition,
                    order_by=order_by,
                    order_by_asc=order_by_asc,
                    dataset_types=dataset_types,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedDatasetList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets'}  # type: ignore

    @distributed_trace_async
    async def register(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        register_as_pending: Optional[bool] = False,
        if_exists_ok: Optional[bool] = True,
        update_definition_if_exists: Optional[bool] = False,
        with_data_hash: Optional[bool] = False,
        user_version_id: Optional[str] = None,
        body: Optional["_models.Dataset"] = None,
        **kwargs: Any
    ) -> "_models.Dataset":
        """Register new dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param register_as_pending:
        :type register_as_pending: bool
        :param if_exists_ok:
        :type if_exists_ok: bool
        :param update_definition_if_exists:
        :type update_definition_if_exists: bool
        :param with_data_hash:
        :type with_data_hash: bool
        :param user_version_id:
        :type user_version_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.Dataset
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dataset, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Dataset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Dataset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'Dataset')
        else:
            _json = None

        request = build_register_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            content_type=content_type,
            json=_json,
            register_as_pending=register_as_pending,
            if_exists_ok=if_exists_ok,
            update_definition_if_exists=update_definition_if_exists,
            with_data_hash=with_data_hash,
            user_version_id=user_version_id,
            template_url=self.register.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Dataset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    register.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets'}  # type: ignore


    @distributed_trace_async
    async def delete_all_datasets(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        **kwargs: Any
    ) -> None:
        """Unregister all datasets in the workspace.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_all_datasets_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            template_url=self.delete_all_datasets.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_all_datasets.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets'}  # type: ignore


    @distributed_trace_async
    async def update_dataset(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        dataset_id: str,
        force_update: Optional[bool] = False,
        body: Optional["_models.Dataset"] = None,
        **kwargs: Any
    ) -> "_models.Dataset":
        """Update a dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :param force_update:
        :type force_update: bool
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.Dataset
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dataset, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Dataset
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Dataset"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'Dataset')
        else:
            _json = None

        request = build_update_dataset_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_id=dataset_id,
            content_type=content_type,
            json=_json,
            force_update=force_update,
            template_url=self.update_dataset.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Dataset', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_dataset.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}'}  # type: ignore


    @distributed_trace_async
    async def unregister_dataset(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        name: str,
        **kwargs: Any
    ) -> None:
        """Unregister a dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param name:
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_unregister_dataset_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            name=name,
            template_url=self.unregister_dataset.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    unregister_dataset.metadata = {'url': '/dataset/v1.2/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{name}'}  # type: ignore

