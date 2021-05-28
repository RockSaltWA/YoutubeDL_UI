import tkinter as tk
from pytube import YouTube


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.vid_text = tk.Label(self)
        self.vid_text["text"] = "YouTube Downloader by Echo"
        self.vid_text["font"] = "Times"
        self.vid_text.grid(columnspan=3)

        self.vid_url = tk.Entry(self, justify="center")
        self.vid_url.grid(columnspan=2)

        self.uwu = tk.Button(self)
        self.uwu["text"] = "Download"
        self.uwu["command"] = self.hentai_download
        self.uwu.grid(row=1, column=2)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.place(relx=0.5, rely=0.5, anchor="center")
        self.quit.grid(columnspan=3)

        # self.button_bonus = tk.Button(self, text="Bonuses", command=self.download_popup)
        # self.button_bonus.grid(columnspan=3)

    def download_popup(self, title):
        win = tk.Toplevel()
        win.wm_title("Downloading %s", title)

        # l = tk.Label(win, text="Input")
        # l.grid(row=0, column=0)
        #
        # b = tk.Button(win, text="Okay", command=win.destroy)
        # b.grid(row=1, column=0)

    def kaboom_alphabet(self):
        alphabet = []
        for i in range(65, 91):
            alphabet.append(chr(i))
        for i in range(97, 123):
            alphabet.append(chr(i))
        return alphabet

    def hentai_download(self):
        alphabet = self.kaboom_alphabet
        url = self.vid_url.get()
        yt = YouTube(url)
        title = yt.title
        self.download_popup(title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

root = tk.Tk()
root.title("YouTube Downloader")
# root.geometry("852x480")
#loading image logo
root.iconphoto(True, tk.PhotoImage(file ='eyt.png'))
#Resizeable for different monitors
root.resizable(True, True)
app = Application(master=root)
app.mainloop()

