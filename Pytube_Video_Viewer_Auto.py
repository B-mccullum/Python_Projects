from pytube import Youtube  # Import the Youtube class from the pytube library
from sys import argv  # Import the argv module from the sys library

link = argv[1]  # Get the YouTube link from the command line arguments
yt = Youtube(link)  # Create a new Youtube object with the provided link

print("Title: ", yt.title)  # Print the title of the YouTube video

print("View: ", yt.views)  # Print the number of views of the YouTube video

yd = yt.streams.get_highest_resolution()  # Get the stream with the highest resolution

yd.download()  # Download the YouTube video using the highest resolution stream
