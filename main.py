import os
from pytube import YouTube
from youtubesearchpython import VideosSearch

query = input("Type the query: ")
search = VideosSearch(query, limit=1)
if search.result()['result']:
    video_url = search.result()['result'][0]['link']
    print("url:" + video_url)
    
else:
    print('No video link found for query:', query)


# replace with your video URL
yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
print("Installing...")
video.download(output_path='.', filename='px.audio.mp3')

print("playing... ({})".format(yt.title))
os.system("bash player.sh &> /dev/null &")
data = "null"
while data != "stop":
    data = input("Type stop for stop music: ")
    if data == "stop":
        os.system("bash -c '[[ $(ps -aux | grep px.audio.mp3 | head -n 1) =~ \"px.audio.mp3\" ]] && echo 'stoping...' && touch stop'")

print("Done.")
