# YouTube-downloader
Download videos and mp3 from YouTube

# Dependencies
[pytube](https://pytube.io/en/latest/)
[moviepy](https://pypi.org/project/moviepy/)

# issues
YouTube Videos doesn't have audio codec with every streams. For different resolutions without audio, audio and video are seperately downloaded and merged using moviepy module. It is a little slow.
Tried ffmpeg, but [Exception: filenotfounderror: [WinError 2] The system cannot find the file specified](https://stackoverflow.com/questions/66982682/ffmpeg-winerror-2-the-system-cannot-find-the-file-specified?rq=1)
