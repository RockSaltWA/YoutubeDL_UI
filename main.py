from tkinter import *
from pytube import *
import video_conversion

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.dropdown_variable2 = StringVar(self)
        self.bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", ".", "~"]
        self.dropdown_variable1 = StringVar(self)
        self.master = master

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.vid_text = Label(self)
        self.vid_text["text"] = "YouTube Downloader by Echo"
        self.vid_text["font"] = "Times"
        self.vid_text.grid(columnspan=3)

        self.vid_url = Entry(self, justify="center")
        self.vid_url.grid(columnspan=2)

        self.uwu = Button(self)
        self.uwu["text"] = "Download"
        self.uwu["command"] = self.download_manager
        self.uwu.grid(row=1, column=2)

        # self.statusbutton = Button(self)
        # self.statusbutton["text"] = "Status"
        # self.statusbutton["command"] = self.download_manager
        # self.statusbutton.grid(row=5, column=0)

        self.dropdown_variable1.set("<file type>")
        self.dropdown_filetype = OptionMenu(self, self.dropdown_variable1, "mp4", "mp3", "png (thumbnail)")
        self.dropdown_filetype.grid(row=2, column=2)

        self.dropdown_variable2.set("<link type>")
        self.dropdown_linktype = OptionMenu(self, self.dropdown_variable2, "playlist", "video")
        self.dropdown_linktype.grid(row=2, column=0)

        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.place(relx=0.5, rely=0.5, anchor="center")
        self.quit.grid(columnspan=3)

    def download_manager(self):
        filetype, linktype = self.dropdown_status()
        print("hello")
        if linktype == "video":
            if filetype == "mp4":
                self.mp4_download(YouTube(self.vid_url.get()))
            elif filetype == "mp3":
                self.mp3_download()
        elif linktype == "playlist":
            if filetype == "mp4":
                p = Playlist(self.vid_url.get())
                for video in p.videos:
                    self.mp4_download(video)
            elif filetype == "mp3":
                pass
        else:
            print("Wrong shit ig idek")
            self.master.destroy()

    def dropdown_status(self):
        filetype = self.dropdown_variable1.get()
        linktype = self.dropdown_variable2.get()
        return filetype, linktype

    def download_popup(self, title):
        # win = tk.Toplevel()
        # win.wm_title("Downloading %s", title)
        pass

    def mp4_download(self, yt):
        video_conversion.missing_dir("./mp4")
        title = yt.title
        print("downloading mp4")
        for i in self.bad_chars:
            title = title.replace(i, '')
        # self.download_popup(title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("./mp4")
        print("downloaded %s.mp4" % title)
        # video_display.MyVideoCapture("./" + title + ".mp4")

    def mp3_download(self):
        video_conversion.missing_dir("./temp")
        yt = YouTube(self.vid_url.get())
        title = yt.title
        print("downloading mp3")
        for i in self.bad_chars:
            title = title.replace(i, '')
        self.download_popup(title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("./temp")
        video_conversion.mp4_2_mp3(title)
        print("downloaded %s.mp4" % title)


root = Tk()
root.title("YouTube Downloader")
root.geometry("852x480")

# loading image logo
root.iconphoto(True, PhotoImage(file='eyt.png'))

# Resizeable for different monitors
root.resizable(True, True)
app = Application(master=root)
app.mainloop()