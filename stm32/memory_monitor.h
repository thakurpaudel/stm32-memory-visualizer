
#ifndef MEMORY_MONITOR_H
#define MEMORY_MONITOR_H

#include <stdint.h>

typedef struct
{
    uint32_t heap_start;
    uint32_t heap_end;
    uint32_t heap_limit;

    uint32_t stack_top;
    uint32_t stack_pointer;
    uint32_t stack_limit;

    uint32_t free_heap;
    uint32_t used_heap;
    uint32_t used_stack;
} memory_snapshot_t;

void MemoryMonitor_Init(void);
void MemoryMonitor_GetSnapshot(memory_snapshot_t *snap);
void MemoryMonitor_PrintUART(void);

#endif
