#File Manager
#By @Thomas

from typing import Coroutine
from sys import path
import shutil
import os
print("Welcome, To File Manager By Thomas!")
print("----------------------------------")
Currnt_dir = os.path.dirname(os.path.realpath(__file__))
print(Currnt_dir)
for filename in os.listdir(Currnt_dir):

    # FOR Photos

    if filename.endswith((".png", "jpg")):
        if not os.path.exists("Photos"):
            os.mkdir('Photos')
        shutil.copy(filename, "Photos")
        os.remove(filename)
        print("Done Photos File..")

# --------------------------------------

    # FOR Videos

    if filename.endswith((".MP4")):
        if not os.path.exists("Videos"):
            os.mkdir("Videos")
        shutil.copy(filename, "Videos")
        os.remove(filename)
        print("Done Videos File..")
