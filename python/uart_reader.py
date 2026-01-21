import serial
import re

pattern = re.compile(
    r"HEAP_START=0x([0-9A-F]+).*HEAP_END=0x([0-9A-F]+).*STACK_SP=0x([0-9A-F]+)"
)

def read_uart(port):
    ser = serial.Serial(port, 115200, timeout=1)
    while True:
        line = ser.readline().decode(errors="ignore")
        m = pattern.search(line)
        if m:
            yield (
                int(m.group(1), 16),
                int(m.group(2), 16),
                int(m.group(3), 16),
            )

