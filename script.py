#extracting covers
'''from mutagen.mp3 import MP3
from mutagen.id3 import ID3
audio = MP3("demons.mp3")
file = ID3("demons.mp3")
rez = audio.tags['APIC:'].data
with open('image.jpg', 'wb') as img:
   img.write(rez)
print(audio)'''

import librosa
from io import StringIO
import numpy as np
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("Demons.mp3", mono=False)
fig, ax = plt.subplots(sharex=True)
title = "abc"
ax.set(title=title)
ax.label_outer()
fig.set_figheight(6)
fig.set_figwidth(18)
librosa.display.waveshow(y, sr=sr, ax=ax)
print(type(librosa.display.waveshow(y, sr=sr, ax=ax)))
plt.show()