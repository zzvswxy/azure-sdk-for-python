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

class CheckNameAvailabilityReason(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The reason why the given name is not available.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class CommunicationServicesProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the resource.
    """

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    RUNNING = "Running"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DomainManagement(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes how a Domains resource is being managed.
    """

    AZURE_MANAGED = "AzureManaged"
    CUSTOMER_MANAGED = "CustomerManaged"
    CUSTOMER_MANAGED_IN_EXCHANGE_ONLINE = "CustomerManagedInExchangeOnline"

class DomainsProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the resource.
    """

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    RUNNING = "Running"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"

class EmailServicesProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the resource.
    """

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    RUNNING = "Running"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    MOVING = "Moving"

class KeyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The keyType to regenerate. Must be either 'primary' or 'secondary'(case-insensitive).
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class Origin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class UserEngagementTracking(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes whether user engagement tracking is enabled or disabled.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class VerificationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the verification operation.
    """

    NOT_STARTED = "NotStarted"
    VERIFICATION_REQUESTED = "VerificationRequested"
    VERIFICATION_IN_PROGRESS = "VerificationInProgress"
    VERIFICATION_FAILED = "VerificationFailed"
    VERIFIED = "Verified"
    CANCELLATION_REQUESTED = "CancellationRequested"

class VerificationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of verification.
    """

    DOMAIN = "Domain"
    SPF = "SPF"
    DKIM = "DKIM"
    DKIM2 = "DKIM2"
    DMARC = "DMARC"
