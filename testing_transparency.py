from pytube import *
import moviepy.editor as mp

clip = mp.VideoFileClip("./mp4/ads.mp4")
clip.audio.write_audiofile("5050.wav")
#
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# print("hi")
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("./mp3")