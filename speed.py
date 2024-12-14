from moviepy.editor import *
from moviepy.video.fx.all import speedx

video = VideoFileClip("KRSK DS-I456Z 39_20241214-143245--20241214-143345SUB5000_30000.avi")

# Ускорение видео в 2 раза
video_fast = video.fx(speedx, 2)
video_fast.write_videofile("fast_video.mp4")
