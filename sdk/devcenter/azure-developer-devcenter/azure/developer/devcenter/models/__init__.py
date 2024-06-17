# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import Catalog
from ._models import DevBox
from ._models import DevBoxAction
from ._models import DevBoxActionDelayResult
from ._models import DevBoxNextAction
from ._models import Environment
from ._models import EnvironmentDefinition
from ._models import EnvironmentDefinitionParameter
from ._models import EnvironmentType
from ._models import Error
from ._models import HardwareProfile
from ._models import ImageReference
from ._models import InnerError
from ._models import OSDisk
from ._models import OperationDetails
from ._models import Pool
from ._models import Project
from ._models import RemoteConnection
from ._models import Schedule
from ._models import StopOnDisconnectConfiguration
from ._models import StorageProfile

from ._enums import DevBoxActionDelayStatus
from ._enums import DevBoxActionType
from ._enums import DevBoxProvisioningState
from ._enums import EnvironmentProvisioningState
from ._enums import EnvironmentTypeStatus
from ._enums import HibernateSupport
from ._enums import LocalAdministratorStatus
from ._enums import OSType
from ._enums import OperationStatus
from ._enums import ParameterType
from ._enums import PoolHealthStatus
from ._enums import PowerState
from ._enums import ScheduledFrequency
from ._enums import ScheduledType
from ._enums import SkuName
from ._enums import StopOnDisconnectStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Catalog",
    "DevBox",
    "DevBoxAction",
    "DevBoxActionDelayResult",
    "DevBoxNextAction",
    "Environment",
    "EnvironmentDefinition",
    "EnvironmentDefinitionParameter",
    "EnvironmentType",
    "Error",
    "HardwareProfile",
    "ImageReference",
    "InnerError",
    "OSDisk",
    "OperationDetails",
    "Pool",
    "Project",
    "RemoteConnection",
    "Schedule",
    "StopOnDisconnectConfiguration",
    "StorageProfile",
    "DevBoxActionDelayStatus",
    "DevBoxActionType",
    "DevBoxProvisioningState",
    "EnvironmentProvisioningState",
    "EnvironmentTypeStatus",
    "HibernateSupport",
    "LocalAdministratorStatus",
    "OSType",
    "OperationStatus",
    "ParameterType",
    "PoolHealthStatus",
    "PowerState",
    "ScheduledFrequency",
    "ScheduledType",
    "SkuName",
    "StopOnDisconnectStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
