from io import StringIO
import numpy as np
import os
import random
import sys
import time
from videoreader import VideoReader

frame_count = (lambda: VideoReader(
    '/home/sppmacd/Videos/badapple.webm').number_of_frames)()
terminal_size = (lambda: [int(i) for i in open("terminal_size.txt").read().split()])()

FUNCTION_NAMES = [
    "i",
    "up",
    "get",
    "load",
    "parse",
    "format"
]

lead_size = len("   10 |     frame<     >(\"")

os.makedirs("sources", exist_ok=True)

def rand_op():
    chars = "+-*/%"
    return chars[random.randrange(len(chars))]

FRAMES_PER_FILE = 200
FRAME_REPETITIONS = 1

for i in range(int(frame_count / FRAMES_PER_FILE) + 1):
    with open(f"sources/badapple_{i:03}.txt", "w") as ascii_file:
        for j in range(FRAMES_PER_FILE):
            frame = i * FRAMES_PER_FILE + j
            print(f"Generating: Frame {frame}/{frame_count} ({frame*100/frame_count:.1f}%)")

            try:
                with open(f"frames/{frame}", "rb") as frame_file:
                    frame_data = frame_file.read()
            except FileNotFoundError:
                break

            # FANCY        
            data = StringIO()

            offset = 0
            while offset < len(frame_data) - 2:
                if frame_data[offset] < 10:
                    data.write(" ")
                    offset += 1
                else:
                    longest_white_sequence = 0
                    offset2 = offset
                    while offset2 < len(frame_data) - 2 and frame_data[offset2] >= 10:
                        longest_white_sequence += 1
                        offset2 += 1

                    trailing_length = len("() + ")

                    while longest_white_sequence > 0:
                        required_function_name_length = longest_white_sequence - trailing_length
                        if required_function_name_length <= 0:
                            data.write(f" " * longest_white_sequence)
                            break
                        elif required_function_name_length < len(FUNCTION_NAMES):
                            data.write(f"{FUNCTION_NAMES[required_function_name_length - 1]}() {rand_op()} ")
                            break
                        else:
                            length = random.randrange(1, len(FUNCTION_NAMES) + 1)
                            data.write(f"{FUNCTION_NAMES[length - 1]}() {rand_op()} ")
                            longest_white_sequence -= length + trailing_length

                    offset = offset2

            for _ in range(FRAME_REPETITIONS):
                ascii_file.write(f"    frame<{frame:5}>(")
                ascii_file.write(" "*(terminal_size[0] - lead_size))
                ascii_file.write(data.getvalue())
                ascii_file.write("2);\n")

    # PLAIN
    # ascii_file.write(f"    frame<{i:5.0f}>(")
    # ascii_file.write(" "*(terminal_size[0] - lead_size))
    # for pixel in frame_data:
    #     ascii_file.write("#" if pixel > 10 else " ")
    # ascii_file.write(");\n")

for i in range(int(frame_count / FRAMES_PER_FILE) + 1):
    with open(f"sources/badapple_{i:03}.cpp", "w") as source_file:
        template = open("template.cpp").read()
        template = template.replace("|FRAMES|", open(f"sources/badapple_{i:03}.txt").read())
        source_file.write(template)
