import numpy as np
import os
import sys
import time
from videoreader import VideoReader

video = VideoReader('/home/sppmacd/Videos/badapple.webm')
frame_count = video.number_of_frames
terminal_size = (lambda: [int(i) for i in open("terminal_size.txt").read().split()])()

x_step = video.frame_width / (terminal_size[0])
y_step = video.frame_height / (terminal_size[1] - 8)

os.makedirs("frames", exist_ok=True)

for frame in video:
    print(f"Preprocessing: Frame {video.current_frame_pos}/{frame_count} ({video.current_frame_pos*100/frame_count:.1f}%)")

    with open(f"frames/{int(video.current_frame_pos - 1)}", "wb") as image:
        # TODO: Interpolate
        for scanline_idx in np.arange(0, video.frame_height, y_step):
            scanline = frame[int(scanline_idx)]
            for pixel_idx in np.arange(0, video.frame_width, x_step):
                pixel = scanline[int(pixel_idx)]
                image.write(bytes([pixel[0]]))
