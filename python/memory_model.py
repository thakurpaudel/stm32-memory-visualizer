class MemoryModel:
    def __init__(self, ram_start, ram_end):
        self.ram_start = ram_start
        self.ram_end = ram_end

        self.heap_start = None
        self.heap_end = None
        self.stack_sp = None

    def update(self, heap_start, heap_end, stack_sp):
        self.heap_start = heap_start
        self.heap_end = heap_end
        self.stack_sp = stack_sp

