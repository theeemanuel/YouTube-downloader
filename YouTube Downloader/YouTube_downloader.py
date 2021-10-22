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
    try:
        os.makedirs("downloads")
        print("New Folder 'downloads', created")
    except Exception:
        print("Clearing old 'temp' files")
    try:
        os.makedirs("temp")
    except Exception:
        print("Opening 'downloads' folder")
    try:
        for f in os.listdir('temp'):
            os.remove(os.path.join('temp', f))
    except Exception:
        print()
    vid = YouTube(url)
    video = YouTube(url).streams.filter(res=res).first().download('temp')
    filename = vid.title
    for subString in filename:
        if subString == '/':
            filename = filename.replace('/','-',1)
        if subString == '|':
            filename = filename.replace('|','-',1)
        if subString == ':':
            filename = filename.replace(':','-',1)
    directory = 'downloads/'+str(filename)+'.mp4'
    print(directory)
    os.rename(video,"temp/video.mp4")
    audio = YouTube(url).streams.filter(only_audio=True).first().download('temp')
    os.rename(audio,"temp/audio.mp3")
    video_stream = mpe.VideoFileClip('temp/video.mp4')
    audio_stream = mpe.AudioFileClip('temp/audio.mp3')
    output = video_stream.set_audio(audio_stream)
    output.write_videofile(str(directory))
    os.remove("temp/audio.mp3")
    try:
        os.remove("temp/video.mp4")
    except Exception:
        print("Can't clear cache files")

def musicList(url):
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

def download_playlist(url, res):
    try:
        for f in os.listdir('temp'):
            os.remove(os.path.join('temp', f))
    except Exception:
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
            vid = video.streams.filter(res=res).first().download('temp')
            i += 1
            os.rename(vid,'temp/'+str(i)+'video.mp4')
            aud = video.streams.filter(only_audio=True).first().download('temp')
            os.rename(aud,'temp/'+str(i)+'audio.mp3')
            video_stream = mpe.VideoFileClip('temp/'+str(i)+'video.mp4')
            audio_stream = mpe.AudioFileClip('temp/'+str(i)+'audio.mp3')
            output = video_stream.set_audio(audio_stream)
            output.write_videofile(str(playlist.title)+'/'+str(i)+'.mp4')
            os.remove('temp/'+str(i)+'audio.mp3')
            try:
                os.remove('temp/'+str(i)+'video.mp4')
            except Exception:
                print("Can't clear cache files")
            
        except Exception:
            print("Could find it in "+str(res))
            print("redownloading '"+str(video_url)+"' in highest resolution...")
            vid = video.streams.get_highest_resolution().download('temp')
            i += 1
            os.rename(vid,'temp/'+str(i)+'video.mp4')
            aud = video.streams.filter(only_audio=True).first().download('temp')
            os.rename(aud,'temp/'+str(i)+'audio.mp3')
            video_stream = mpe.VideoFileClip('temp/'+str(i)+'video.mp4')
            audio_stream = mpe.AudioFileClip('temp/'+str(i)+'audio.mp3')
            output = video_stream.set_audio(audio_stream)
            output.write_videofile(str(playlist.title)+'/'+str(i)+'.mp4')
            os.remove('temp/'+str(i)+'audio.mp3')
            try:
                os.remove('temp/'+str(i)+'video.mp4')
            except Exception:
                print("Can't clear cache files")

run = True
while run:
    print()
    url = str(input("Enter the video/playlist link: "))

    if "playlist" in url:
        res = str(input("Enter choice of resolution (or audio): "))
        if res == 'audio':
            musicList(url)
        else:
            download_playlist(url, res)
        print()
        print()
        print("Downloaded all files!")
    
    else:
        video = YouTube(url)
        print()
        print("Searching for available resolutions for ")
        print("'"+str(video.title)+"'")
        print(resolution(url))
        print()
        res = str(input("Enter choice of resolution (or for only audio, enter audio): "))
    
        if res == 'audio':
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
        else:
            download(url, res)
            print()
        print("Downloaded!")
    reply = str(input("Do you have another video/playlist/audio to download?(y/n) "))
    if reply == 'y' or reply == 'Y':
        run = True
        print("______________________________________________________________________")
    else:
        run = False
    
