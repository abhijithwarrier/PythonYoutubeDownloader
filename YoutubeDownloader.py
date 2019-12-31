# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    linkLabel = Label(root, text="YOUTUBE LINK  :", bg="deepskyblue4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    destinationLabel = Label(root, text="DESTINATION    :", bg="deepskyblue4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)

    browseButton = Button(root, text="BROWSE", command=Browse, width=15)
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    dwldButton = Button(root, text="DOWNLOAD", command=Download, width=30)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)

# Defining Browse() to select a destination folder to save the video
def Browse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in downloadDirectory
    downloadDirectory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    # Displaying the directory in the directory textbox
    downloadPath.set(downloadDirectory)

# Defining Download() to download the video
def Download():
    # Fetching the user-input Youtube Link and storing it in yt_link variable
    yt_link = videoLink.get()
    # Fetching the Destination Directory and storing it in dwldFolder variable
    dwldFolder = downloadPath.get()

    # Creating object of YouTube() with the yt_link variable as the argument
    getVideo = YouTube(yt_link)

    # Getting all the available streams of the youtube video and selecting the first from the
    # filtered streams using first()
    videoStream = getVideo.streams.first()

    # Downloading the video to the user-input destination directory
    videoStream.download(dwldFolder)

    # Displaying the message
    messagebox.showinfo("SUCCESS", "VIDEO DOWNLOADED AND SAVED IN\n" + dwldFolder)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window and disabling the
# resizing property
root.geometry("650x120")
root.resizable(False, False)
root.title("PyYoutubeDownloader")
root.config(background="deepskyblue4")

# Creating the tkinter Variables
videoLink = StringVar()
downloadPath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
