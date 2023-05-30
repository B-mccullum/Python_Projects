# for this code I used Pycharm in combination with Pytube to download the Youtube videos onto my local computer.

from pytube import Youtube
from sys import argv

link = argv[1]
yt = Youtube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download()

#insert the file path using forward slashes and single '' quotations in between the parentheses on line 15.

# on the terminal command line enter the custom folder name (YT.py, for example) followed by the the link to the youtube video in '' single quotations that you want to save offline and press enter.
# the youtube video will be downloaded into your local file and be available to watch.
