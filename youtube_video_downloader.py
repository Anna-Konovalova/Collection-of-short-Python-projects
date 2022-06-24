#Importing pytube3 library
from pytube import YouTube

#Getting video link
user_link = input("Enter the link to the video you want to download: ")
yt = YouTube(user_link)

#Checking video details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", round(yt.length/60), "minutes")
print("Rating: ", yt.rating)
print("File size in highest resolution: ", (yt.streams.get_highest_resolution().filesize)*0.000001, " MB")
#print("Available resolution: ", yt.streams.filter(only_video=True))
print()
#print("Description: ", yt.description)

#Downloading video
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download()
print("Download complete!")

#The video will be saved in the working directory. 
#To select a different directory use: ys.download('location') specifying the absolute path
