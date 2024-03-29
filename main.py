import urllib
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Progressbar

from pytube import *
import video_conversion

"""
To do list (or just random improvements to the code:

1. Impliment a progress bar or something for each file
2. Progress bar for playlist
3. Report the amount of videos in playlist
4. Show the video in question in a label bar
5. Display image thumbnail while downloading video along with title and length (perhaps size???)
6. Encoding subtitle tracks in mp4 downloads (optional, not default???)
"""


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.dropdown_variable2 = StringVar(self)
        self.bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", ".", "~", "$"]
        self.dropdown_variable1 = StringVar(self)
        self.master = master

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas()
        # self.canvas.grid(row=0, column=0, rowspan=3, columnspan=6)

        self.background_image = PhotoImage(file="background.png")
        self.background_label = Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.perc_prog = 0

        self.vid_text = Label(self)
        self.vid_text["text"] = "Enter url:"
        self.vid_text["highlightthickness"] = 0
        self.vid_text.grid(row=0, column=0, padx=5, pady=5, sticky=W + N)

        self.vid_url = Entry(self, justify="center", width=50)
        self.vid_url.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky=N)

        self.uwu = Button(self)
        self.uwu["text"] = "Download"
        self.uwu["command"] = self.download_manager
        self.uwu.grid(row=2, column=0, columnspan=4, padx=5, pady=5, stick=W + E)

        self.dropdown_variable1.set("<select file type>")
        self.dropdown_filetype = OptionMenu(self, self.dropdown_variable1, "mp4", "mp3", "wav", "png (thumbnail)")
        self.dropdown_filetype.config(width=20)
        self.dropdown_filetype["highlightthickness"] = 0
        self.dropdown_filetype["justify"] = "center"
        self.dropdown_filetype.grid(row=1, column=0, columnspan=2, padx=5, pady=5, stick=W)

        self.dropdown_variable2.set("<select link type>")
        self.dropdown_linktype = OptionMenu(self, self.dropdown_variable2, "playlist", "video")
        self.dropdown_linktype.config(width=20)
        self.dropdown_linktype["highlightthickness"] = 0
        self.dropdown_linktype["justify"] = "center"
        self.dropdown_linktype.grid(row=1, column=2, columnspan=2, padx=5, pady=5, stick=E)

        # self.progress = Progressbar(self, orient=HORIZONTAL, length=100, mode="determinate", variable=self.perc_prog)
        # self.progress.grid(row=3, column=0, columnspan=4, padx=5, pady=5, stick=W + S + E)

        # self.logo = PhotoImage(file='cropFunky2.png')
        # self.logo_label = Label(self, image=self.logo)
        # self.logo_label["highlightthickness"] = 0
        # self.logo_label.grid(row=0, column=4, rowspan=3, columnspan=1, ipadx=5, pady=5, sticky=N+E+S)

        # self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.place(relx=0.5, rely=0.5, anchor="center")
        # self.quit.grid(columnspan=3)

    def download_manager(self):
        if not video_conversion.connect("https://youtube.com"):
            showerror("Error: No connection to YouTube", "Check your internet and ensure that YouTube servers are functioning")
            return 0
        else:
            filetype, linktype = self.dropdown_status()
        if self.vid_url.get() == "":
            print("No url scrub")
            self.error_popup("Error: No url given", "Please enter a url")
        if linktype == "video":
            if filetype == "mp4":
                # self.mp4_download(YouTube(self.vid_url.get(), on_progress_callback=self.progress_function))
                self.mp4_download(YouTube(self.vid_url.get()))
            elif filetype == "mp3":
                self.mp3_download(YouTube(self.vid_url.get()))
            elif filetype == "wav":
                self.wav_download(YouTube(self.vid_url.get()))
            elif filetype == "png (thumbnail)":
                self.thumbnail_download(YouTube(self.vid_url.get()))
        elif linktype == "playlist":
            if filetype == "mp4":
                p = Playlist(self.vid_url.get())
                for video in p.videos:
                    self.mp4_download(video)
            elif filetype == "mp3":
                p = Playlist(self.vid_url.get())
                for video in p.videos:
                    self.mp3_download(video)
            elif filetype == "wav":
                p = Playlist(self.vid_url.get())
                for video in p.videos:
                    self.wav_download(video)
            elif filetype == "png (thumbnail)":
                p = Playlist(self.vid_url.get())
                for video in p.videos:
                    self.thumbnail_download(video)
        elif linktype == "<select link type>":
            print("No linktype")
            self.error_popup("Error: No link type selected", "Please select a link type")
        elif filetype == "<select file type>":
            print("No filetype")
            self.error_popup("Error: No file type selected", "Please select a file type")

    def dropdown_status(self):
        filetype = self.dropdown_variable1.get()
        linktype = self.dropdown_variable2.get()
        return filetype, linktype


    """
    Not working, can try to impliment this in a future date
    """

    def error_popup(self, title, text):
        showerror(title, text)

    def mp4_download(self, yt):
        video_conversion.missing_dir("./mp4")
        title = yt.title
        print("downloading mp4")
        for i in self.bad_chars:
            title = title.replace(i, '')
        # self.download_popup(title)
        try:
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
                "./mp4")
        except:
            showerror("Error: unable to find stream", "Check your connection and ensure the link is valid and public")
        print("downloaded %s.mp4" % title)
        # video_display.MyVideoCapture("./" + title + ".mp4")

    def mp3_download(self, yt):
        video_conversion.missing_dir("./temp")
        title = yt.title
        print("downloading mp3")
        for i in self.bad_chars:
            title = title.replace(i, '')
        # self.download_popup(title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            "./temp")
        video_conversion.mp4_2_mp3(title)
        print("downloaded %s.mp4" % title)

    def wav_download(self, yt):
        video_conversion.missing_dir("./temp")
        title = yt.title
        print("downloading wav")
        for i in self.bad_chars:
            title = title.replace(i, '')
        # self.download_popup(title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            "./temp")
        video_conversion.mp4_2_wav(title)
        print("downloaded %s.mp4" % title)

    """
    Thumbnail downloader for yt ui
    """

    def thumbnail_download(self, yt):
        video_conversion.missing_dir("./thumbnails")
        title = yt.title
        print("downloading thumbnail")
        for i in self.bad_chars:
            title = title.replace(i, '')
        # self.download_popup(title)
        url = yt.thumbnail_url
        print(url)
        urllib.request.urlretrieve(url, "./thumbnails/%s.png" % title)

    # def bar(self):
    #     while(0):
    #

    def calc_percent(self, tem, total):
        self.perc_prog = (float(tem) / float(total)) * float(100)

    def progress_function(self, stream, chunk, file_handle, bytes_remaining):
        size = stream.filesize
        p = 0
        while p < 100:
            progress = p
            print
            str(p) + '%'
            p = self.calc_percent(bytes_remaining, size)
        if p == 100:
            p = 0
            self.perc_prog = 0


root = Tk()
root.title("£cho's YouTube Downloader")
# root.geometry("852x480")

# loading image logo
root.iconphoto(True, PhotoImage(file='eyt.png'))

# Resizeable for different monitors
root.resizable(False, False)
app = Application(master=root)
app.mainloop()
