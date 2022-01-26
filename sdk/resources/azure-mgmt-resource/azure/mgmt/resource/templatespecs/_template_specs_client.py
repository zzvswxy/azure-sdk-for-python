# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import TemplateSpecsClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class TemplateSpecsClient(MultiApiClientMixin, _SDKClient):
    """The APIs listed in this specification can be used to manage Template Spec resources through the Azure Resource Manager.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2021-05-01'
    _PROFILE_TAG = "azure.mgmt.resource.templatespecs.TemplateSpecsClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url="https://management.azure.com",  # type: str
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        self._config = TemplateSpecsClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(TemplateSpecsClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-06-01-preview: :mod:`v2019_06_01_preview.models<azure.mgmt.resource.templatespecs.v2019_06_01_preview.models>`
           * 2021-03-01-preview: :mod:`v2021_03_01_preview.models<azure.mgmt.resource.templatespecs.v2021_03_01_preview.models>`
           * 2021-05-01: :mod:`v2021_05_01.models<azure.mgmt.resource.templatespecs.v2021_05_01.models>`
        """
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview import models
            return models
        elif api_version == '2021-03-01-preview':
            from .v2021_03_01_preview import models
            return models
        elif api_version == '2021-05-01':
            from .v2021_05_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def template_spec_versions(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TemplateSpecVersionsOperations<azure.mgmt.resource.templatespecs.v2019_06_01_preview.operations.TemplateSpecVersionsOperations>`
           * 2021-03-01-preview: :class:`TemplateSpecVersionsOperations<azure.mgmt.resource.templatespecs.v2021_03_01_preview.operations.TemplateSpecVersionsOperations>`
           * 2021-05-01: :class:`TemplateSpecVersionsOperations<azure.mgmt.resource.templatespecs.v2021_05_01.operations.TemplateSpecVersionsOperations>`
        """
        api_version = self._get_api_version('template_spec_versions')
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TemplateSpecVersionsOperations as OperationClass
        elif api_version == '2021-03-01-preview':
            from .v2021_03_01_preview.operations import TemplateSpecVersionsOperations as OperationClass
        elif api_version == '2021-05-01':
            from .v2021_05_01.operations import TemplateSpecVersionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'template_spec_versions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def template_specs(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TemplateSpecsOperations<azure.mgmt.resource.templatespecs.v2019_06_01_preview.operations.TemplateSpecsOperations>`
           * 2021-03-01-preview: :class:`TemplateSpecsOperations<azure.mgmt.resource.templatespecs.v2021_03_01_preview.operations.TemplateSpecsOperations>`
           * 2021-05-01: :class:`TemplateSpecsOperations<azure.mgmt.resource.templatespecs.v2021_05_01.operations.TemplateSpecsOperations>`
        """
        api_version = self._get_api_version('template_specs')
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TemplateSpecsOperations as OperationClass
        elif api_version == '2021-03-01-preview':
            from .v2021_03_01_preview.operations import TemplateSpecsOperations as OperationClass
        elif api_version == '2021-05-01':
            from .v2021_05_01.operations import TemplateSpecsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'template_specs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
