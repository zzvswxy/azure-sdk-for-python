# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AvailableOperation
    from ._models_py3 import AvailableOperationDisplay
    from ._models_py3 import AvailableOperationDisplayPropertyServiceSpecificationMetricsItem
    from ._models_py3 import AvailableOperationDisplayPropertyServiceSpecificationMetricsList
    from ._models_py3 import AvailableOperationsListResponse
    from ._models_py3 import CSRPError
    from ._models_py3 import CSRPErrorBody
    from ._models_py3 import CustomizationHostName
    from ._models_py3 import CustomizationIPAddress
    from ._models_py3 import CustomizationIPSettings
    from ._models_py3 import CustomizationIdentity
    from ._models_py3 import CustomizationIdentityUserData
    from ._models_py3 import CustomizationNicSetting
    from ._models_py3 import CustomizationPoliciesListResponse
    from ._models_py3 import CustomizationPolicy
    from ._models_py3 import CustomizationSpecification
    from ._models_py3 import DedicatedCloudNode
    from ._models_py3 import DedicatedCloudNodeListResponse
    from ._models_py3 import DedicatedCloudService
    from ._models_py3 import DedicatedCloudServiceListResponse
    from ._models_py3 import GuestOSCustomization
    from ._models_py3 import GuestOSNICCustomization
    from ._models_py3 import OperationError
    from ._models_py3 import OperationResource
    from ._models_py3 import PatchPayload
    from ._models_py3 import PrivateCloud
    from ._models_py3 import PrivateCloudList
    from ._models_py3 import ResourcePool
    from ._models_py3 import ResourcePoolsListResponse
    from ._models_py3 import Sku
    from ._models_py3 import SkuAvailability
    from ._models_py3 import SkuAvailabilityListResponse
    from ._models_py3 import Usage
    from ._models_py3 import UsageListResponse
    from ._models_py3 import UsageName
    from ._models_py3 import VirtualDisk
    from ._models_py3 import VirtualDiskController
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineListResponse
    from ._models_py3 import VirtualMachineStopMode
    from ._models_py3 import VirtualMachineTemplate
    from ._models_py3 import VirtualMachineTemplateListResponse
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkListResponse
    from ._models_py3 import VirtualNic
except (SyntaxError, ImportError):
    from ._models import AvailableOperation  # type: ignore
    from ._models import AvailableOperationDisplay  # type: ignore
    from ._models import AvailableOperationDisplayPropertyServiceSpecificationMetricsItem  # type: ignore
    from ._models import AvailableOperationDisplayPropertyServiceSpecificationMetricsList  # type: ignore
    from ._models import AvailableOperationsListResponse  # type: ignore
    from ._models import CSRPError  # type: ignore
    from ._models import CSRPErrorBody  # type: ignore
    from ._models import CustomizationHostName  # type: ignore
    from ._models import CustomizationIPAddress  # type: ignore
    from ._models import CustomizationIPSettings  # type: ignore
    from ._models import CustomizationIdentity  # type: ignore
    from ._models import CustomizationIdentityUserData  # type: ignore
    from ._models import CustomizationNicSetting  # type: ignore
    from ._models import CustomizationPoliciesListResponse  # type: ignore
    from ._models import CustomizationPolicy  # type: ignore
    from ._models import CustomizationSpecification  # type: ignore
    from ._models import DedicatedCloudNode  # type: ignore
    from ._models import DedicatedCloudNodeListResponse  # type: ignore
    from ._models import DedicatedCloudService  # type: ignore
    from ._models import DedicatedCloudServiceListResponse  # type: ignore
    from ._models import GuestOSCustomization  # type: ignore
    from ._models import GuestOSNICCustomization  # type: ignore
    from ._models import OperationError  # type: ignore
    from ._models import OperationResource  # type: ignore
    from ._models import PatchPayload  # type: ignore
    from ._models import PrivateCloud  # type: ignore
    from ._models import PrivateCloudList  # type: ignore
    from ._models import ResourcePool  # type: ignore
    from ._models import ResourcePoolsListResponse  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuAvailability  # type: ignore
    from ._models import SkuAvailabilityListResponse  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageListResponse  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import VirtualDisk  # type: ignore
    from ._models import VirtualDiskController  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineListResponse  # type: ignore
    from ._models import VirtualMachineStopMode  # type: ignore
    from ._models import VirtualMachineTemplate  # type: ignore
    from ._models import VirtualMachineTemplateListResponse  # type: ignore
    from ._models import VirtualNetwork  # type: ignore
    from ._models import VirtualNetworkListResponse  # type: ignore
    from ._models import VirtualNic  # type: ignore

from ._vmware_cloud_simple_enums import (
    AggregationType,
    CustomizationHostNameType,
    CustomizationIPAddressType,
    CustomizationIdentityType,
    CustomizationPolicyPropertiesType,
    DiskIndependenceMode,
    GuestOSNICCustomizationAllocation,
    GuestOSType,
    NICType,
    NodeStatus,
    OnboardingStatus,
    OperationOrigin,
    StopMode,
    UsageCount,
    VirtualMachineStatus,
)

__all__ = [
    'AvailableOperation',
    'AvailableOperationDisplay',
    'AvailableOperationDisplayPropertyServiceSpecificationMetricsItem',
    'AvailableOperationDisplayPropertyServiceSpecificationMetricsList',
    'AvailableOperationsListResponse',
    'CSRPError',
    'CSRPErrorBody',
    'CustomizationHostName',
    'CustomizationIPAddress',
    'CustomizationIPSettings',
    'CustomizationIdentity',
    'CustomizationIdentityUserData',
    'CustomizationNicSetting',
    'CustomizationPoliciesListResponse',
    'CustomizationPolicy',
    'CustomizationSpecification',
    'DedicatedCloudNode',
    'DedicatedCloudNodeListResponse',
    'DedicatedCloudService',
    'DedicatedCloudServiceListResponse',
    'GuestOSCustomization',
    'GuestOSNICCustomization',
    'OperationError',
    'OperationResource',
    'PatchPayload',
    'PrivateCloud',
    'PrivateCloudList',
    'ResourcePool',
    'ResourcePoolsListResponse',
    'Sku',
    'SkuAvailability',
    'SkuAvailabilityListResponse',
    'Usage',
    'UsageListResponse',
    'UsageName',
    'VirtualDisk',
    'VirtualDiskController',
    'VirtualMachine',
    'VirtualMachineListResponse',
    'VirtualMachineStopMode',
    'VirtualMachineTemplate',
    'VirtualMachineTemplateListResponse',
    'VirtualNetwork',
    'VirtualNetworkListResponse',
    'VirtualNic',
    'AggregationType',
    'CustomizationHostNameType',
    'CustomizationIPAddressType',
    'CustomizationIdentityType',
    'CustomizationPolicyPropertiesType',
    'DiskIndependenceMode',
    'GuestOSNICCustomizationAllocation',
    'GuestOSType',
    'NICType',
    'NodeStatus',
    'OnboardingStatus',
    'OperationOrigin',
    'StopMode',
    'UsageCount',
    'VirtualMachineStatus',
]