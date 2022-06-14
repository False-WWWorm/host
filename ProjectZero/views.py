import os
from mutagen.mp3 import MP3

from django.shortcuts import render

def index(request):
    listall = os.listdir("assets/audio")
    arr_len = {}
    for i in listall:
        path = "assets/audio/" + i
        ex = int(MP3(path).info.length)
        arr_len[i] = str(ex // 60) + ":" + str(ex % 60).zfill(2)
    pl = []
    for i in listall:
        temp = []
        temp.append(i)
        temp.append(arr_len[i])
        temp.append(os.path.splitext(i)[0])
        pl.append(temp)

    col = ["Playlist1", "Sadness", "hardbass"]
    data = {"pl":pl, "col":col, }
    return render(request, 'index.html', context=data)
def test(request):
    pl = os.listdir("assets/audio")
    data = {"pl":pl, }
    return render(request, 'test.html', context=data)