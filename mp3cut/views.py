import requests
from django.shortcuts import render
from django.shortcuts import redirect
from pydub import AudioSegment
from mutagen.mp3 import MP3

def mp3cut(request):
    def cutmp3(*args):
        bitrate = str(int(MP3(file_name).info.bitrate / 1000)) + "k"

        startMin = int(strtMn)
        startSec = int(strtSc)

        endMin = int(em)
        endSec = int(es)

        startTime = startMin * 60 * 1000 + startSec * 1000
        endTime = endMin * 60 * 1000 + endSec * 1000

        song = AudioSegment.from_mp3(file_name)
        extract = song[startTime:endTime]

        extract.export(file_name + "-edited.mp3", format="mp3", bitrate=bitrate)


    name = request.POST.get("id").split()
    file_name = "assets/audio/" + str(name[0])
    strtMn = name[1][:1]
    strtSc = name[1][2:]
    em = name[2][:1]
    es = name[2][2:]
    cutmp3(file_name, strtSc, strtMn, em, es)
    #return redirect('/')
    return render(request, 'mp3cut/mp3cut.html')

def index(request):
    return render(request, 'index.html')