# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class AppResourceProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the App
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CREATING = "Creating"
    UPDATING = "Updating"

class ConfigServerState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the config server.
    """

    NOT_AVAILABLE = "NotAvailable"
    DELETED = "Deleted"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"

class DeploymentResourceProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the Deployment
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class DeploymentResourceStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the Deployment
    """

    UNKNOWN = "Unknown"
    STOPPED = "Stopped"
    RUNNING = "Running"
    FAILED = "Failed"
    ALLOCATING = "Allocating"
    UPGRADING = "Upgrading"
    COMPILING = "Compiling"

class ManagedIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the managed identity
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class MonitoringSettingState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the Monitoring Setting.
    """

    NOT_AVAILABLE = "NotAvailable"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the Service
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    DELETED = "Deleted"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    MOVING = "Moving"
    MOVED = "Moved"
    MOVE_FAILED = "MoveFailed"

class ResourceSkuRestrictionsReasonCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the reason for restriction. Possible values include: 'QuotaId',
    'NotAvailableForSubscription'
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class ResourceSkuRestrictionsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the type of restrictions. Possible values include: 'Location', 'Zone'
    """

    LOCATION = "Location"
    ZONE = "Zone"

class RuntimeVersion(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Runtime version
    """

    JAVA8 = "Java_8"
    JAVA11 = "Java_11"
    NET_CORE31 = "NetCore_31"

class SkuScaleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the type of the scale.
    """

    NONE = "None"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"

class SupportedRuntimePlatform(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The platform of this runtime version (possible values: "Java" or ".NET").
    """

    JAVA = "Java"
    _NET_CORE = ".NET Core"

class SupportedRuntimeValue(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The raw value which could be passed to deployment CRUD operations.
    """

    JAVA8 = "Java_8"
    JAVA11 = "Java_11"
    NET_CORE31 = "NetCore_31"

class TestKeyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the test key
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class TrafficDirection(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The direction of required traffic
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

class UserSourceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the source uploaded
    """

    JAR = "Jar"
    NET_CORE_ZIP = "NetCoreZip"
    SOURCE = "Source"
