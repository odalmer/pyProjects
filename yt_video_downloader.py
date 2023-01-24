import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

link = input("Enter the yt video link: ")
yt = YouTube(link)

# This is to get the folder path
# creates a hidden main window
root = tk.Tk() 
# hide the main window
root.withdraw() 
# opens the file explorer dialog and allows the user to select a folder.
folder_path = filedialog.askdirectory() 

print("Title: ", yt.title)
print("Views: ", yt.views/1000000 + "M")
print("Please wait")

yd = yt.streams.get_highest_resolution()
yd.download(folder_path)
