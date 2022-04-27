# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
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
from ...operations._extensions_operations import build_create_request, build_delete_request, build_get_request, build_list_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ExtensionsOperations:
    """ExtensionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models
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
    async def create(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, "_models.Enum0"],
        cluster_resource_name: Union[str, "_models.Enum1"],
        cluster_name: str,
        extension_instance_name: str,
        extension_instance: "_models.ExtensionInstance",
        **kwargs: Any
    ) -> "_models.ExtensionInstance":
        """Create a new Kubernetes Cluster Extension Instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :param extension_instance: Properties necessary to Create an Extension Instance.
        :type extension_instance:
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstance
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExtensionInstance, or the result of cls(response)
        :rtype: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstance
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExtensionInstance"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(extension_instance, 'ExtensionInstance')

        request = build_create_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_instance_name=extension_instance_name,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ExtensionInstance', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, "_models.Enum0"],
        cluster_resource_name: Union[str, "_models.Enum1"],
        cluster_name: str,
        extension_instance_name: str,
        **kwargs: Any
    ) -> "_models.ExtensionInstance":
        """Gets details of the Kubernetes Cluster Extension Instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExtensionInstance, or the result of cls(response)
        :rtype: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstance
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExtensionInstance"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_instance_name=extension_instance_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ExtensionInstance', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, "_models.Enum0"],
        cluster_resource_name: Union[str, "_models.Enum1"],
        cluster_name: str,
        extension_instance_name: str,
        extension_instance: "_models.ExtensionInstanceUpdate",
        **kwargs: Any
    ) -> "_models.ExtensionInstance":
        """Update an existing Kubernetes Cluster Extension Instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :param extension_instance: Properties to Update in the Extension Instance.
        :type extension_instance:
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstanceUpdate
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExtensionInstance, or the result of cls(response)
        :rtype: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstance
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExtensionInstance"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(extension_instance, 'ExtensionInstanceUpdate')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_instance_name=extension_instance_name,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ExtensionInstance', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, "_models.Enum0"],
        cluster_resource_name: Union[str, "_models.Enum1"],
        cluster_name: str,
        extension_instance_name: str,
        **kwargs: Any
    ) -> None:
        """Delete a Kubernetes Cluster Extension Instance. This will cause the Agent to Uninstall the
        extension instance from the cluster.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
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

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            extension_instance_name=extension_instance_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, "_models.Enum0"],
        cluster_resource_name: Union[str, "_models.Enum1"],
        cluster_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.ExtensionInstancesList"]:
        """List all Source Control Configurations.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExtensionInstancesList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstancesList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExtensionInstancesList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    cluster_rp=cluster_rp,
                    cluster_resource_name=cluster_resource_name,
                    cluster_name=cluster_name,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    cluster_rp=cluster_rp,
                    cluster_resource_name=cluster_resource_name,
                    cluster_name=cluster_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ExtensionInstancesList", pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions'}  # type: ignore
