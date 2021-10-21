from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mpe

def resolution(url):
    video = YouTube(url)

    res = []
    for stream in video.streams.order_by('resolution'):
        res.append(stream.resolution)
    resSet = set(res)
    
    return resSet

def download(url, res):
    video = YouTube(url).streams.filter(res=res).first().download()
    filename = str(video.title)+'.mp4'
    os.rename(video,"video.mp4")
    audio = YouTube(url).streams.filter(only_audio=True).first().download()
    os.rename(audio,"audio.mp3")
    video_stream = mpe.VideoFileClip('video.mp4')
    audio_stream = mpe.AudioFileClip('audio.mp3')
    output = video_stream.set_audio(audio_stream)
    output.write_videofile('output.mp4')
    os.remove("audio.mp3")
    os.remove("video.mp4")
    os.rename('output.mp4',filename)

def download_playlist(url, res):
    print()
    playlist = Playlist(url)
    try:
        os.makedirs(playlist.title)
    except OSError:
        pass
    print('Downloading %s videos...' % len(playlist.video_urls))
    i = 0
    for video_url in playlist.video_urls:
        print()
        print("downloading...",video_url)
        video = YouTube(video_url)
        try:
            vid = video.streams.filter(res=res).first().download()
            i += 1
            filename = str(playlist.title)+'/'+str(video.title)+'.mp4'
            os.rename(vid,'video.mp4')
            aud = video.streams.filter(only_audio=True).first().download()
            os.rename(aud,'audio.mp3')
            video_stream = mpe.VideoFileClip('video.mp4')
            audio_stream = mpe.AudioFileClip('audio.mp3')
            output = video_stream.set_audio(audio_stream)
            output.write_videofile(str(playlist.title)+'/'+str(i)+'.mp4')
            os.remove('audio.mp3')
            os.remove('video.mp4')
            
        except Exception:
            print("Could find it in "+str(res))
            print("redownloading '"+str(video_url)+"' in highest resolution...")
            vid = video.streams.get_highest_resolution().download()
            i += 1
            filename = str(playlist.title)+'/'+str(video.title)+'.mp4'
            os.rename(vid,str(i)+'video.mp4')
            aud = video.streams.filter(only_audio=True).first().download()
            os.rename(aud,str(i)+'audio.mp3')
            video_stream = mpe.VideoFileClip(str(i)+'video.mp4')
            audio_stream = mpe.AudioFileClip(str(i)+'audio.mp3')
            output = video_stream.set_audio(audio_stream)
            output.write_videofile(str(playlist.title)+'/'+str(i)+'.mp4')
            os.remove(str(i)+'audio.mp3')
            os.remove(str(i)+'video.mp4')

print()
url = str(input("Enter the video/playlist link: "))

if "playlist" in url:
    res = str(input("Enter choice of resolution: "))
    print()
    download_playlist(url, res)
    print()
    print()
    print("Downloaded all videos!")
    
else:
    video = YouTube(url)
    print()
    print("Searching for available resolutions for ")
    print("'"+str(video.title)+"'")
    print(resolution(url))
    print()
    res = str(input("Enter choice of resolution (or for only audio, enter audio): "))
    
    if res == 'audio':
        audio = video.streams.filter(only_audio=True).first().download()
        os.rename(audio, str(video.title)+".mp3")
    else:
        download(url, res)
        print()

    print("Downloaded!")
