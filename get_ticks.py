import socket
import json
from datetime import datetime
import time

TICKS_PER_SLOT = 64

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 9000))

last_slot = None
slot_start_ns = None

print("Listening for ticks on UDP port 9000...\n")

while True:
    data, _ = sock.recvfrom(1024)
    try:
        tick = json.loads(data.decode())
        tick_height = tick["tick_height"]
        slot = tick["slot"]
        ts_ns = tick["timestamp_ns"]

        now_ns = time.time_ns()
        latency_ns = now_ns - ts_ns
        latency_us = latency_ns / 1_000

        if tick_height % TICKS_PER_SLOT == 0:
            if last_slot is not None:
                duration_ns = ts_ns - slot_start_ns
                duration_ms = duration_ns / 1_000_000
                print(f"Slot {last_slot} duration: {duration_ms:.3f} ms")
            print(f"New slot started: {slot} at {ts_ns} (poh socket latency: {latency_us:.2f} µs)")
            last_slot = slot
            slot_start_ns = ts_ns
        #else:
            #print(f"Tick {tick_height} (slot {slot}) latency: {latency_us:.2f} µs")

    except Exception as e:
        print("Error parsing tick:", e)
