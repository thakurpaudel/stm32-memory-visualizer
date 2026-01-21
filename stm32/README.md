
# STM32 Memory Visualizer

A real-time **heap, stack, and flash memory visualization tool** for STM32 embedded projects.

This tool helps developers **understand, debug, and demonstrate** how memory is actually used inside a running microcontroller — beyond what IDEs and map files show.

---

## Features

-  Live RAM visualization (heap / stack / static sections)
-  Tracks real `malloc`, `free`, `new`, `delete`, `pvPortMalloc`
-  Uses linker symbols (`_end`, `_estack`)
-  Detects heap–stack collision risk
-  UART-based real-time monitoring
-  Simulation mode (no hardware needed)
-  Works with FreeRTOS and bare-metal

---

##  Why This Exists

Most STM32 developers rely on:
- Map files
- Guessing stack size
- IDE memory views

This project answers:
> *What is REALLY happening to memory at runtime?*

---

##  Architecture Overview

