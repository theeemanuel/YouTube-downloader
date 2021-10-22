# YouTube-downloader
Download videos and mp3 from YouTube

# mp3-downloader
Only for downloading mp3s, you can use it in your android/ios device:
- download '[pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)' and '[pydroid repository plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3.quickinstallrepo)'
- open pydroid 3, in the sandwitch option menu, open 'pip' and install '[pytube](https://pytube.io/en/latest/)' library
- open [mp3-downloader.py](https://github.com/theeemanuel/YouTube-downloader/blob/main/YouTube%20Downloader/mp3-downloader.py) and run it  


# Dependencies
- [pytube](https://pytube.io/en/latest/) cmd: pip install pytube
- [moviepy](https://pypi.org/project/moviepy/) cmd: pip install moviepy

# issues
YouTube Videos doesn't have audio codec with every streams. For different resolutions without audio, audio and video are seperately downloaded and merged using moviepy module. It is a little slow.
Tried ffmpeg, but [Exception: filenotfounderror: [WinError 2] The system cannot find the file specified](https://stackoverflow.com/questions/66982682/ffmpeg-winerror-2-the-system-cannot-find-the-file-specified?rq=1)
