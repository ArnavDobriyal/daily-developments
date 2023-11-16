from pytube import YouTube
a=input("input url")
yt=YouTube(a)
stream = yt.streams.get_highest_resolution()
stream.download(output_path='C:\\Users\\dobri\\Videos\\downloadedvideo')
print(yt.title)