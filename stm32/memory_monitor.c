
#include "memory_monitor.h"
#include "stm32f4xx_hal.h"
#include <stdio.h>

/* linker symbols */
extern uint8_t _end;
extern uint8_t _estack;
extern uint32_t _Min_Stack_Size;

/* heap pointer used by _sbrk */
extern uint8_t *__sbrk_heap_end;

static UART_HandleTypeDef *dbg_uart;

static inline uint32_t get_sp(void)
{
    uint32_t sp;
    __asm volatile ("mrs %0, msp" : "=r"(sp));
    return sp;
}

void MemoryMonitor_Init(void)
{
    /* assign UART used for debug */
    extern UART_HandleTypeDef huart2;
    dbg_uart = &huart2;
}

void MemoryMonitor_GetSnapshot(memory_snapshot_t *snap)
{
    uint32_t stack_top = (uint32_t)&_estack;
    uint32_t stack_limit = stack_top - (uint32_t)&_Min_Stack_Size;
    uint32_t sp = get_sp();

    uint32_t heap_start = (uint32_t)&_end;
    uint32_t heap_end   = (uint32_t)__sbrk_heap_end;
    uint32_t heap_limit = stack_limit;

    snap->heap_start   = heap_start;
    snap->heap_end     = heap_end;
    snap->heap_limit   = heap_limit;
    snap->used_heap    = heap_end - heap_start;
    snap->free_heap    = heap_limit - heap_end;

    snap->stack_top     = stack_top;
    snap->stack_pointer= sp;
    snap->stack_limit  = stack_limit;
    snap->used_stack   = stack_top - sp;
}

void MemoryMonitor_PrintUART(void)
{
    memory_snapshot_t s;
    MemoryMonitor_GetSnapshot(&s);

    char buf[256];

    int len = snprintf(buf, sizeof(buf),
        "HEAP_START=0x%08lX "
        "HEAP_END=0x%08lX "
        "HEAP_USED=%lu "
        "STACK_SP=0x%08lX "
        "STACK_USED=%lu\r\n",
        s.heap_start,
        s.heap_end,
        s.used_heap,
        s.stack_pointer,
        s.used_stack
    );

    HAL_UART_Transmit(dbg_uart, (uint8_t *)buf, len, HAL_MAX_DELAY);
}
