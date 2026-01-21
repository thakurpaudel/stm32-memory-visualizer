import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
import random

# RAM example addresses (STM32F4)
RAM_START = 0x24000000
RAM_END   = 0x24080000

# Static sections
DATA_START = RAM_START
DATA_END   = DATA_START + 0x2000   # 8 KB
BSS_START  = DATA_END
BSS_END    = BSS_START + 0x2000    # 8 KB

HEAP_START = BSS_END
STACK_TOP  = RAM_END
STACK_LIMIT = STACK_TOP - 0x400    # minimum stack

# Initialize heap and stack
heap_end = HEAP_START
stack_ptr = STACK_TOP
max_stack_used = 0
max_stack_ptr = STACK_TOP

fig, ax = plt.subplots(figsize=(3, 8))
plt.ion()

for t in range(50):
    ax.clear()

    # Simulate heap growth
    heap_end += random.randint(0, 0x100)
    if heap_end > STACK_LIMIT:
        heap_end = STACK_LIMIT

    # Simulate stack usage
    stack_ptr -= random.randint(0, 0x80)
    if stack_ptr < heap_end:
        stack_ptr = heap_end

    # Update max stack
    stack_used = STACK_TOP - stack_ptr
    if stack_used > (STACK_TOP - max_stack_ptr):
        max_stack_ptr = stack_ptr

    # Draw RAM picture
    ax.add_patch(patches.Rectangle((0, DATA_START), 1, DATA_END - DATA_START, facecolor='pink'))
    ax.add_patch(patches.Rectangle((0, BSS_START), 1, BSS_END - BSS_START, facecolor='lightgreen'))
    ax.add_patch(patches.Rectangle((0, HEAP_START), 1, heap_end - HEAP_START, facecolor='skyblue'))
    ax.add_patch(patches.Rectangle((0, stack_ptr), 1, STACK_TOP - stack_ptr, facecolor='orange'))
    ax.add_patch(patches.Rectangle((0, heap_end), 1, stack_ptr - heap_end, facecolor='lightgray'))

    # Max stack line
    ax.axhline(y=max_stack_ptr, color='red', linestyle='--', linewidth=2)
    ax.text(0.5, max_stack_ptr, 'Max Stack', color='red', va='bottom', ha='center')

    # Labels
    ax.text(0.5, DATA_START + (DATA_END - DATA_START)/2, '.data', ha='center', va='center')
    ax.text(0.5, BSS_START + (BSS_END - BSS_START)/2, '.bss', ha='center', va='center')
    ax.text(0.5, HEAP_START + (heap_end - HEAP_START)/2, 'heap', ha='center', va='center')
    ax.text(0.5, stack_ptr + (STACK_TOP - stack_ptr)/2, 'stack', ha='center', va='center')

    ax.set_ylim(RAM_START, RAM_END)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylabel('RAM Address')
    ax.set_title('STM32 RAM Picture with Max Stack Indicator')
    plt.pause(0.1)

plt.ioff()
plt.show()

