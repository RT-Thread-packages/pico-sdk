#!/usr/bin/env python3
import os
import re
import shutil

# create src/common/pico_base/include/pico/config_autogen.h
f = open('src/common/pico_base/include/pico/config_autogen.h', 'w')
f.write('#include "boards/pico.h"\n')
f.close()

with open('pico_sdk_version.cmake', 'r') as f:
    contents = f.read()

    major_match = re.search(r'set\(PICO_SDK_VERSION_MAJOR (\d+)\)', contents)
    minor_match = re.search(r'set\(PICO_SDK_VERSION_MINOR (\d+)\)', contents)
    revision_match = re.search(r'set\(PICO_SDK_VERSION_REVISION (\d+)\)', contents)

    major_version = major_match.group(1)
    minor_version = minor_match.group(1)
    revision_version = revision_match.group(1)

# replace the version numbers in src/common/pico_base/include/pico/version.h
with open('src/common/pico_base/include/pico/version.h.in', 'r') as f:
    contents = f.read()

with open('src/common/pico_base/include/pico/version.h', 'w') as f:
    contents = contents.replace('${PICO_SDK_VERSION_MAJOR}', major_version)
    contents = contents.replace('${PICO_SDK_VERSION_MINOR}', minor_version)
    contents = contents.replace('${PICO_SDK_VERSION_REVISION}', revision_version)
    contents = contents.replace('${PICO_SDK_VERSION_STRING}', f'{major_version}.{minor_version}.{revision_version}')
    f.write(contents)
