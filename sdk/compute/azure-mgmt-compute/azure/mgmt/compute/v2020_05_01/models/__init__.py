# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessUri
from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import CreationData
from ._models_py3 import Disk
from ._models_py3 import DiskAccess
from ._models_py3 import DiskAccessList
from ._models_py3 import DiskAccessUpdate
from ._models_py3 import DiskEncryptionSet
from ._models_py3 import DiskEncryptionSetList
from ._models_py3 import DiskEncryptionSetUpdate
from ._models_py3 import DiskList
from ._models_py3 import DiskSku
from ._models_py3 import DiskUpdate
from ._models_py3 import Encryption
from ._models_py3 import EncryptionSetIdentity
from ._models_py3 import EncryptionSettingsCollection
from ._models_py3 import EncryptionSettingsElement
from ._models_py3 import GrantAccessData
from ._models_py3 import ImageDiskReference
from ._models_py3 import InnerError
from ._models_py3 import KeyVaultAndKeyReference
from ._models_py3 import KeyVaultAndSecretReference
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ShareInfoElement
from ._models_py3 import Snapshot
from ._models_py3 import SnapshotList
from ._models_py3 import SnapshotSku
from ._models_py3 import SnapshotUpdate
from ._models_py3 import SourceVault

from ._compute_management_client_enums import AccessLevel
from ._compute_management_client_enums import DiskCreateOption
from ._compute_management_client_enums import DiskEncryptionSetIdentityType
from ._compute_management_client_enums import DiskState
from ._compute_management_client_enums import DiskStorageAccountTypes
from ._compute_management_client_enums import EncryptionType
from ._compute_management_client_enums import HyperVGeneration
from ._compute_management_client_enums import NetworkAccessPolicy
from ._compute_management_client_enums import OperatingSystemTypes
from ._compute_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._compute_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._compute_management_client_enums import SnapshotStorageAccountTypes
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessUri",
    "ApiError",
    "ApiErrorBase",
    "CreationData",
    "Disk",
    "DiskAccess",
    "DiskAccessList",
    "DiskAccessUpdate",
    "DiskEncryptionSet",
    "DiskEncryptionSetList",
    "DiskEncryptionSetUpdate",
    "DiskList",
    "DiskSku",
    "DiskUpdate",
    "Encryption",
    "EncryptionSetIdentity",
    "EncryptionSettingsCollection",
    "EncryptionSettingsElement",
    "GrantAccessData",
    "ImageDiskReference",
    "InnerError",
    "KeyVaultAndKeyReference",
    "KeyVaultAndSecretReference",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "Resource",
    "ShareInfoElement",
    "Snapshot",
    "SnapshotList",
    "SnapshotSku",
    "SnapshotUpdate",
    "SourceVault",
    "AccessLevel",
    "DiskCreateOption",
    "DiskEncryptionSetIdentityType",
    "DiskState",
    "DiskStorageAccountTypes",
    "EncryptionType",
    "HyperVGeneration",
    "NetworkAccessPolicy",
    "OperatingSystemTypes",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "SnapshotStorageAccountTypes",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
