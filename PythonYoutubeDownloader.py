# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO DOWNLOAD VIDEOS FROM YOUTUBE WITH THE VIDEO LINK USING pytube MODULE and PLAY THE
# DOWNLOADED VIDEO IN THE APPLICATION WINDOW.
#
# pytube is a very serious, lightweight, dependency-free Python library (command-line utility)
# for downloading YouTube Videos. It has no third party dependencies & aims to be highly reliable.
# pytube also makes pipelining easy, allowing to specify callback functions for different
# download events, such as on progress or on complete.
#
# The module can be installed using the command - pip install pytube
#
# P.S - IN CASE YOU GET AN ERROR RELATED TO KeyError 'CIPHER',
# open the extract.py file mentioned in the Error and on line no. 301 replace 'cipher' keyword in
# parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats) with signatureCipher keyword
# parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)

# Importing necessary packages
import cv2
import datetime
import tkinter as tk
from tkinter import *
from pytube import YouTube
from PIL import Image,ImageTk
from tkinter import messagebox, filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    linkLabel = Label(root, text="YOUTUBE LINK  :", bg="tan4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=57, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    destinationLabel = Label(root, text="DESTINATION    :", bg="tan4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=40, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)

    browseButton = Button(root, text="BROWSE", command=Browse, width=15)
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    dwldButton = Button(root, text="DOWNLOAD", command=Download, width=30)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)

    root.videoLabel = Label(root, bg="tan4")
    root.videoLabel.grid(row=4, columnspan=3, padx = 5, pady = 5, column=0)

# Defining Browse() to select a destination folder to save the video
def Browse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in downloadDirectory
    downloadDirectory = filedialog.askdirectory(initialdir="/Users/abhijithwarrier/Movies")
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
    # Storing the name for the downloaded video in the videoName variable
    videoName = str(datetime.datetime.now().strftime('%d%m%y%H%M%S'))
    # Storing the current datetime value as start_time
    start_time = datetime.datetime.now()
    # Downloading the video to the user-input destination directory
    videoStream.download(dwldFolder, filename=videoName)
    # Storing the current datetime value as end_time
    end_time = datetime.datetime.now()
    # Calculating and storing the difference between the start_time and end_time as total_time
    total_time = (end_time - start_time).seconds
    # Displaying the message
    messagebox.showinfo("SUCCESS", "VIDEO DOWNLOADED AND SAVED IN\n" + dwldFolder +
                        "\nDOWNLOAD TIME : " + str(total_time) + " SECONDS")
    # Creating object of class VideoCapture with webcam index
    root.cap = cv2.VideoCapture(dwldFolder + '/' +videoName + '.mp4')
    # Calling the PlayVideo() function to play the downloaded video
    PlayVideo()

def PlayVideo():
    #Capturing frame by frame
    ret1, frame1 = root.cap.read()
    # Fetching the width and height of the video frames
    width = root.cap.get(3)
    height = root.cap.get(4)
    resize_width = int(width)
    resize_height = int(height)
    # Resizing the video frame
    video = cv2.resize(frame1,(resize_width,resize_height), fx=0,fy=0,
                       interpolation = cv2.INTER_CUBIC)
    # Converting the frame from BGR TO original RGBA
    video = cv2.cvtColor(video,cv2.COLOR_BGR2RGBA)
    # Creating an image memory from the above frame exporting array interface
    videoImg = Image.fromarray(video)
    # Creating object of PhotoImage() class to display the frame
    imgtk = ImageTk.PhotoImage(image = videoImg)
    # Configuring the label to display the frame
    root.videoLabel.configure(image = imgtk)
    # Keeping a reference
    root.videoLabel.imgtk = imgtk
    # Calling the function after 10 milliseconds
    root.videoLabel.after(32, PlayVideo)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window
# and disabling the resizing property of the tkinter window
root.geometry("665x490")
root.title("PyYoutubeDownloader")
root.config(background="tan4")
root.resizable(False, False)

# Creating the tkinter Variables
videoLink = StringVar()
downloadPath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
