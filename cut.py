# https://github.com/jiaaro/pydub

from pydub import AudioSegment
from mutagen.mp3 import MP3

def cutmp3 (file_name):
    # Bitrate like str "256k"
    bitrate = str(int(MP3(file_name).info.bitrate / 1000))+"k"
    #bitrate = "128k"

    startMin = 0
    startSec = 0

    endMin = 1
    endSec = 25

    # Time to miliseconds
    startTime = startMin*60*1000+startSec*1000
    endTime = endMin*60*1000+endSec*1000

    # Opening file and extracting segment
    song = AudioSegment.from_mp3(file_name)
    extract = song[startTime:endTime]

    # Saving
    extract.export( file_name + "-ch.mp3", format="mp3", bitrate=bitrate)

track_for_cut = "assets/audio/test.mp3"
cutmp3(track_for_cut)