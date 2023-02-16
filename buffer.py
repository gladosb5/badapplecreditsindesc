import os
import sys
import time

terminal_size = (lambda: [int(i) for i in open("terminal_size.txt").read().split()])()
FRAME_TIME = 1/30

while True:
    start_time = time.time()
    out = ""
    for i in range(7):
        out += (sys.stdin.readline() or exit())
    sys.stdout.write(out or exit())
    time.sleep(FRAME_TIME - (time.time() - start_time))
