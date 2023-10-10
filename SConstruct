import os
import re
import shutil

PREFIX = 'arm-none-eabi-'
EXEC_PATH = ''
if os.getenv('RTT_EXEC_PATH'):
    EXEC_PATH = os.getenv('RTT_EXEC_PATH')

env = Environment(
CC = PREFIX + 'gcc',
AS = PREFIX + 'gcc',
AR = PREFIX + 'ar', ARFLAGS = '-rc',
CXX = PREFIX + 'g++',
LINK = PREFIX + 'gcc',
TARGET_EXT = 'elf',
SIZE = PREFIX + 'size',
OBJDUMP = PREFIX + 'objdump',
OBJCPY = PREFIX + 'objcopy',
CCFLAGS=Split('''
-mcpu=cortex-m0plus
-mthumb
-O3 
-DNDEBUG
-Wl,--build-id=none 
--specs=nosys.specs 
-nostartfiles
-Wl,
-Wl,-Map=bs2_default.elf.map
'''),
LINKFLAGS=Split('''
-mcpu=cortex-m0plus
-mthumb
-O3 
-DNDEBUG
--specs=nosys.specs 
-nostartfiles
-Tsrc/rp2_common/boot_stage2/boot_stage2.ld
'''),
CPPDEFINES = Split('''
PICO_BOARD=\"pico\"
PICO_BUILD=1
PICO_NO_HARDWARE=0
DPICO_ON_DEVICE=1
'''),
CPPPATH = Split('''
src/rp2_common/boot_stage2/asminclude
src/rp2040/hardware_regs/include
src/rp2_common/hardware_base/include 
src/common/pico_base/include
src/boards/include
src/rp2_common/pico_platform/include
src/rp2_common/boot_stage2/include
src/boards/include
''')
)
env.PrependENVPath('PATH', EXEC_PATH)

env.Command(
    ['src/common/pico_base/include/pico/config_autogen.h','src/common/pico_base/include/pico/version.h'],
    '',
    'python3 tools/generate_headers.py'
)

env.Program(
    'bs2_default.elf',
    ['src/rp2_common/boot_stage2/compile_time_choice.S'],
)

env.Command(
    'bs2_default.bin',
    'bs2_default.elf',
    env['OBJCPY'] + ' -Obinary bs2_default.elf bs2_default.bin',
)

env.Command(
    'bs2_default_padded_checksummed.S',
    'bs2_default.bin',
    'python3 src/rp2_common/boot_stage2/pad_checksum -s 0xffffffff bs2_default.bin bs2_default_padded_checksummed.S',
)