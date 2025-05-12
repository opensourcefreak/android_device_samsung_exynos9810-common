#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)

namespace_imports = [
    'device/samsung/exynos9810-common',
    'hardware/samsung',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/hw/rild': blob_fixup()
        .replace_needed('libril.so', 'libril-samsung.so'),
    (
    'vendor/lib/libsensorlistener.so',
    'vendor/lib64/libsensorlistener.so',
    ): blob_fixup()
        .add_needed('libshim_sensorndkbridge.so'),
    (
    'vendor/lib64/libexynosdisplay.so',
    'vendor/lib/libexynosdisplay.so',
    'vendor/lib/hw/hwcomposer.exynos9810.so',
    'vendor/lib64/hw/hwcomposer.exynos9810.so',
    'vendor/lib/sensors.bio.so',
    'vendor/lib/sensors.grip.so',
    'vendor/lib64/sensors.bio.so',
    'vendor/lib64/sensors.grip.so',
    ): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/lib/libaboxpcmdump.so': blob_fixup()
        .add_needed('libaboxpcmdump_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'exynos9810-common',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
