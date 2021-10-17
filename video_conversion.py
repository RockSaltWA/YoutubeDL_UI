import urllib
import imageio_ffmpeg
from PIL.Image import Image
from pydub import *
from moviepy.editor import *
import moviepy.editor as mp


def connect(host='http://youtube.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def missing_dir(dir_path):
    if not os.path.isdir(dir_path):
        print("oh no ur missing a directory so we made it for u uwu")
        os.mkdir(dir_path)


def clean_house(dir_path, mp4_temp):
    os.remove(mp4_temp)
    os.rmdir(dir_path)


def mp4_2_mp3(title):
    missing_dir("./mp3")
    mp4_file = "./temp/%s.mp4" % title
    our_video = VideoFileClip(mp4_file)
    our_audio = our_video.audio
    mp3_file = './mp3/%s.mp3' % title
    our_audio.write_audiofile(mp3_file)
    our_video.close()
    try:
        clean_house("./temp", "./temp/%s.mp4" % title)
    except:
        print("cannot clean house the temp directory")

def mp4_2_wav(title):
    missing_dir("./wav")
    mp4_file = "./temp/%s.mp4" % title
    clip = mp.VideoFileClip("./temp/%s.mp4" % title)
    clip.audio.write_audiofile("./wav/%s.wav" % title)
    clip.close()
    try:
        clean_house("./temp", "./temp/%s.mp4" % title)
    except:
        print("cannot clean house the wav? directory")