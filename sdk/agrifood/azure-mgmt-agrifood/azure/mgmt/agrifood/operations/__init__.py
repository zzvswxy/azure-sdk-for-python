# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._extensions_operations import ExtensionsOperations
from ._farm_beats_extensions_operations import FarmBeatsExtensionsOperations
from ._farm_beats_models_operations import FarmBeatsModelsOperations
from ._locations_operations import LocationsOperations
from ._operations import Operations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'ExtensionsOperations',
    'FarmBeatsExtensionsOperations',
    'FarmBeatsModelsOperations',
    'LocationsOperations',
    'Operations',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()