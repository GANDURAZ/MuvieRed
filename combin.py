from moviepy.editor import *

clip1 = VideoFileClip("2024-12-14 12-15-50.mp4")
clip2 = VideoFileClip("2024-12-14 12-19-10.mp4")
clip3 = VideoFileClip("2024-12-14 12-19-27.mp4")
clip4 = VideoFileClip("2024-12-14 12-21-16.mp4")
clip5 = VideoFileClip("2024-12-14 12-42-39.mp4")
final = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])

final.write_videofile("comp_vid.mp4")
