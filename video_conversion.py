from PIL.Image import Image
from moviepy.editor import *


def missing_dir(dir_path):
    if not os.path.isdir(dir_path):
        print("oh no ur missing a directory so we made it for u uwu")
        os.mkdir(dir_path)


def clean_house(dir_path):
    for x in os.listdir(dir_path):
        os.remove(os.path.join(dir_path, x))
    os.rmdir(dir_path)


def mp4_2_mp3(title):
    missing_dir("./mp3")
    mp4_file = "./temp/%s.mp4" % title
    our_video = VideoFileClip(mp4_file)
    our_audio = our_video.audio
    mp3_file = './mp3/%s.mp3' % title
    our_audio.write_audiofile(mp3_file)
    try:
        clean_house("./temp")
    except:
        print("cannot clean house the temp directory")


def RBGAImage(path):
    return Image.open(path).convert("RGBA")