from pytube import YouTube
from pytube import Playlist
import os

print()
url = str(input("Enter the YouTube link: "))

try:
    os.makedirs('downloads/')
except OSError:
    pass

if "playlist" in url:
    playlist = Playlist(url)
    try:
        os.makedirs('downloads/'+str(playlist.title))
    except OSError:
        pass
    print()
    print()
    print('Downloading %s mp3s...' % len(playlist.video_urls))
    for music in playlist.video_urls:
        print()
        print("downloading...",music)
        video = YouTube(music)
        audio = video.streams.filter(only_audio=True).first().download('downloads')
        filename = video.title
        for subString in video.title:
            if subString == '/':
                filename = filename.replace('/','-',1)
            if subString == '|':
                filename = filename.replace('|','-',1)
            if subString == ':':
                filename = filename.replace(':','-',1)
        os.rename(audio, 'downloads/'+str(playlist.title)+'/'+str(filename)+'.mp3')
    print()
    print()
    print("Downloaded all files!")

else:
    video = YouTube(url)
    audio = video.streams.filter(only_audio=True).first().download('downloads')
    filename = video.title
    for subString in video.title:
        if subString == '/':
            filename = filename.replace('/','-',1)
        if subString == '|':
            filename = filename.replace('|','-',1)
        if subString == ':':
            filename = filename.replace(':','-',1)
    os.rename(audio, 'downloads/'+str(filename)+'.mp3')
    print("Downloaded!")
