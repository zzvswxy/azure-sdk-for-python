# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import StorageCacheManagementClientConfiguration
from .operations import AscOperationsOperations, AscUsagesOperations, CachesOperations, Operations, SkusOperations, StorageTargetOperations, StorageTargetsOperations, UsageModelsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class StorageCacheManagementClient:    # pylint: disable=too-many-instance-attributes
    """A Storage Cache provides scalable caching service for NAS clients, serving data from either
    NFSv3 or Blob at-rest storage (referred to as "Storage Targets"). These operations allow you to
    manage Caches.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storagecache.operations.Operations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.storagecache.operations.SkusOperations
    :ivar usage_models: UsageModelsOperations operations
    :vartype usage_models: azure.mgmt.storagecache.operations.UsageModelsOperations
    :ivar asc_operations: AscOperationsOperations operations
    :vartype asc_operations: azure.mgmt.storagecache.operations.AscOperationsOperations
    :ivar asc_usages: AscUsagesOperations operations
    :vartype asc_usages: azure.mgmt.storagecache.operations.AscUsagesOperations
    :ivar caches: CachesOperations operations
    :vartype caches: azure.mgmt.storagecache.operations.CachesOperations
    :ivar storage_targets: StorageTargetsOperations operations
    :vartype storage_targets: azure.mgmt.storagecache.operations.StorageTargetsOperations
    :ivar storage_target: StorageTargetOperations operations
    :vartype storage_target: azure.mgmt.storagecache.operations.StorageTargetOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-05-01". Note that overriding this
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
        self._config = StorageCacheManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.usage_models = UsageModelsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.asc_operations = AscOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.asc_usages = AscUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.caches = CachesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.storage_targets = StorageTargetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.storage_target = StorageTargetOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

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
        # type: () -> StorageCacheManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
