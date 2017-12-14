# https://github.com/rg3/youtube-dl/blob/master/README.md#readme

#youtube-dl --extract-audio --audio-format aac https://www.youtube.com/watch?v=TpxX60zIhh0
from __future__ import unicode_literals
import youtube_dl
#youtube-dl-v -i --extract-audio --audio-format mp3 https://www.youtube.com/playlist?list=PLi1FCxGBD-x6HW2OD0534F-NWjKXY2pyo
#youtube-dl --extract-audio --audio-mp3 format https://www.youtube.com/watch?v=TpxX60zIhh0

#youtube-dl --extract-audio https://www.youtube.com/watch?v=TpxX60zIhh0

ydl_opts = {}
options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3
    'outtmpl': '%(id)s',        # name the file the ID of the video
    'noplaylist' : True,}       # only download single song, not playlist
#alias ydl="youtube-dl --extract-audio --audio-format wav"
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=TpxX60zIhh0'])
