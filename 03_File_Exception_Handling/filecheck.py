#os.path.exists

"""
Small program to check file exists

import os

filename = "C:/Users/Bani Kinkar Pani/PycharmProjects/PythonProject/03_File_Exception_Handling/newfile.txt"
if os.path.exists(filename):
    print("file exists")
else:
    print("file does not exist")
"""

#pathlib.Path.exists()

from pathlib import Path
filename = Path("/03_File_Exception_Handling/newfile.txt")

if filename.exists():
    print("file exists")
else:
    print("file does not exist")



