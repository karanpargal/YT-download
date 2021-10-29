from tkinter import *
from pytube import YouTube

gui= Tk()
gui.geometry('700x500')
gui.resizable(0,0)
gui.title("YT Video Downloader")

link=StringVar()

Label(gui, text='Enter the link here', font='arial 20 bold').place(x=220,y=120)
link_enter = Entry(gui, width = 30,textvariable = link).place(x = 250, y = 200)

def download():
    url=YouTube(str(link.get()))
    url.streams.order_by('resolution')
    video=url.streams.get_highest_resolution()
    video.download()
    Label(gui,text="Downloaded", font='arial 20 bold').place(x=260,y=320)

Button(gui,text="Download",font='arial 20 bold',bg='green',padx=2, command=download).place(x=260,y=260)

gui.mainloop()
