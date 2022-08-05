from building import *

# get current directory
cwd = GetCurrentDir()

# The set of source files associated with this SConscript file.
src = Split("""
src/rp2_common/pico_stdlib/stdlib.c
src/rp2_common/hardware_gpio/gpio.c
src/rp2_common/hardware_claim/claim.c
src/rp2_common/hardware_sync/sync.c
src/rp2_common/pico_platform/platform.c
src/rp2_common/hardware_uart/uart.c
src/rp2_common/hardware_spi/spi.c
src/rp2_common/hardware_dma/dma.c
src/rp2_common/hardware_i2c/i2c.c
src/common/pico_time/time.c
src/common/pico_time/timeout_helper.c
src/rp2_common/hardware_timer/timer.c
src/common/pico_sync/sem.c
src/common/pico_sync/lock_core.c
src/common/pico_sync/mutex.c
src/common/pico_sync/critical_section.c
src/common/pico_util/datetime.c
src/common/pico_util/pheap.c
src/common/pico_util/queue.c
src/rp2_common/pico_runtime/runtime.c
src/rp2_common/hardware_clocks/clocks.c
src/rp2_common/hardware_watchdog/watchdog.c
src/rp2_common/hardware_xosc/xosc.c
src/rp2_common/hardware_pll/pll.c
src/rp2_common/hardware_vreg/vreg.c
src/rp2_common/hardware_irq/irq.c
src/rp2_common/pico_printf/printf.c
src/rp2_common/pico_bootrom/bootrom.c
src/rp2_common/pico_double/double_init_rom.c
src/rp2_common/pico_double/double_math.c
src/rp2_common/pico_float/float_aeabi.S
src/rp2_common/pico_float/float_init_rom.c
src/rp2_common/pico_float/float_math.c
src/rp2_common/pico_malloc/pico_malloc.c
src/rp2_common/pico_standard_link/binary_info.c
src/rp2_common/pico_stdio/stdio.c
src/rp2_common/pico_stdio_uart/stdio_uart.c
src/rp2_common/pico_standard_link/new_delete.cpp
src/rp2_common/hardware_irq/irq_handler_chain.S
src/rp2_common/pico_bit_ops/bit_ops_aeabi.S
src/rp2_common/pico_divider/divider.S
src/rp2_common/pico_double/double_aeabi.S
src/rp2_common/pico_double/double_v1_rom_shim.S
src/rp2_common/pico_int64_ops/pico_int64_ops_aeabi.S
src/rp2_common/pico_float/float_v1_rom_shim.S
src/rp2_common/hardware_divider/divider.S
src/rp2_common/pico_mem_ops/mem_ops_aeabi.S
src/rp2_common/pico_standard_link/crt0.S
""")

path = [
     cwd + '/src',
    cwd + '/src/common/pico_stdlib/include',
    cwd + '/src/rp2_common/hardware_gpio/include',
    cwd + '/src/common/pico_base/include',
    cwd + '/src/boards/include',
    cwd + '/src/rp2_common/pico_platform/include',
    cwd + '/src/rp2040/hardware_regs/include',
    cwd + '/src/rp2_common/hardware_base/include',
    cwd + '/src/rp2040/hardware_structs/include',
    cwd + '/src/rp2_common/hardware_claim/include',
    cwd + '/src/rp2_common/hardware_sync/include',
    cwd + '/src/rp2_common/hardware_uart/include',
    cwd + '/src/rp2_common/hardware_dma/include',
    cwd + '/src/rp2_common/hardware_spi/include',
    cwd + '/src/rp2_common/hardware_i2c/include',
    cwd + '/src/rp2_common/hardware_pwm/include',    
    cwd + '/src/rp2_common/hardware_divider/include',
    cwd + '/src/common/pico_time/include',
    cwd + '/src/rp2_common/hardware_timer/include',
    cwd + '/src/common/pico_sync/include',
    cwd + '/src/common/pico_util/include',
    cwd + '/src/rp2_common/pico_runtime/include',
    cwd + '/src/rp2_common/hardware_clocks/include',
    cwd + '/src/rp2_common/hardware_resets/include',
    cwd + '/src/rp2_common/hardware_watchdog/include',
    cwd + '/src/rp2_common/hardware_xosc/include',
    cwd + '/src/rp2_common/hardware_pll/include',
    cwd + '/src/rp2_common/hardware_vreg/include',
    cwd + '/src/rp2_common/hardware_irq/include',
    cwd + '/src/rp2_common/pico_printf/include',
    cwd + '/src/rp2_common/pico_bootrom/include',
    cwd + '/src/common/pico_bit_ops/include',
    cwd + '/src/common/pico_divider/include',
    cwd + '/src/rp2_common/pico_double/include',
    cwd + '/src/rp2_common/pico_int64_ops/include',
    cwd + '/src/rp2_common/pico_float/include',
    cwd + '/src/common/pico_binary_info/include',
    cwd + '/src/rp2_common/pico_stdio/include',
    cwd + '/src/rp2_common/pico_stdio_uart/include',
]

CPPDEFINES = [
    'PICO_NO_BINARY_INFO',
    'PICO_NO_PROGRAM_INFO',
    'PICO_BIT_OPS_PICO=1',
    'PICO_BUILD=1',
    # 'PICO_CMAKE_BUILD_TYPE=\\"Release\\"',
    'PICO_COPY_TO_RAM=0',
    'PICO_CXX_ENABLE_EXCEPTIONS=0',
    'PICO_DIVIDER_HARDWARE=1',
    'PICO_DOUBLE_PICO=1',
    'PICO_FLOAT_PICO=1',
    'PICO_INT64_OPS_PICO=1',
    'PICO_MEM_OPS_PICO=1',
    'PICO_NO_FLASH=0',
    'PICO_NO_HARDWARE=0',
    'PICO_ON_DEVICE=1',
    'PICO_PRINTF_PICO=1',
    'PICO_STDIO_UART=1',
    'PICO_USE_BLOCKED_RAM=0'
]

group = DefineGroup('pico-SDK', src, depend = ['PKG_USING_RASPBERRYPI_PICO_SDK'], CPPPATH = path, CPPDEFINES = CPPDEFINES)

Return('group')
