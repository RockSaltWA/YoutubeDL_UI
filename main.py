from tkinter import *
from pytube import YouTube
import video_display


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", ".", "~"]

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
        self.uwu["command"] = self.mp4_download
        self.uwu.grid(row=1, column=2)

        self.dropdown_variable1 = StringVar(self)
        self.dropdown_variable1.set("<file type>")
        self.dropdown_filetype = OptionMenu(self, self.dropdown_variable1, "mp4", "mp3", "png (thumbnail)")
        self.dropdown_filetype.grid(row=2, column=2)

        self.dropdown_variable2 = StringVar(self)
        self.dropdown_variable2.set("<link type>")
        self.dropdown_linktype = OptionMenu(self, self.dropdown_variable2, "playlist", "video")
        self.dropdown_linktype.grid(row=2, column=0)


        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.place(relx=0.5, rely=0.5, anchor="center")
        self.quit.grid(columnspan=3)

        # self.button_bonus = tk.Button(self, text="Bonuses", command=self.download_popup)
        # self.button_bonus.grid(columnspan=3)

    def download_popup(self, title):
        # win = tk.Toplevel()
        # win.wm_title("Downloading %s", title)
        pass

    def kaboom_alphabet(self):
        alphabet = []
        for i in range(65, 91):
            alphabet.append(chr(i))
        for i in range(97, 123):
            alphabet.append(chr(i))
        return alphabet

    def mp4_download(self):
        alphabet = self.kaboom_alphabet
        yt = YouTube(self.vid_url.get())
        title = yt.title
        for i in self.bad_chars:
            title = title.replace(i, '')
        print(title)
        self.download_popup(title)
        print(title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print(title)
        video_display.MyVideoCapture("./" + title + ".mp4")
        print(title)

    # def mp3_download(self):
    #     alphabet = self.kaboom_alphabet
    #     url = self.vid_url.get()
    #     yt = YouTube(url)
    #     title = yt.title
    #     self.download_popup(title)
    #     yt.streams.filter(progressive=True, file_extension='mp3').order_by('resolution').desc().first().download()


root = Tk()
root.title("YouTube Downloader")
# root.geometry("852x480")

# loading image logo
root.iconphoto(True, PhotoImage(file='eyt.png'))

# Resizeable for different monitors
root.resizable(True, True)
app = Application(master=root)
app.mainloop()

