

import pyttsx3
import os

engine = pyttsx3.init()

pyttsx3.speak("Enter Number to open application")

while True:
    print("Enter Nmuber to open application\n")
    print("""Deatils of which number will open which application :-
    \n1.Microsoft Word \n2.Microsoft Powerpoint \n3.Microsoft Excel 
    4.GOOGLE Chrome \n5.VLC Player \n6.ADOBE Illustrator \n7.ADOBE Photoshop 
    8.Microsoft Edge \n9.Notepad \n10.Postman \n0.For Exit""")

    s = input()
    s = s.upper()
    print(s)

    if ("DON'T" in s) or ("DONT" in s) or ("DO NOT" in s) or ("NOT" in s):
        pyttsx3.speak("Type Again Please Sir")
        print(".")
        print("-!.!-")
        continue

    elif ("0" in s):
        pyttsx3.speak("Exiting the Window")
        break

    elif ("1" in s):
        os.system("start winword")

    elif ("2" in s):
        os.system("start powerpoint")
    
    elif ("3" in s):
        os.system("start excel")

    elif ("4" in s):
        os.system("start chrome")

    elif ("5" in s):
        os.system("start vlc")
    
    elif ("6" in s):
        os.system("start illustrator")
    
    elif ("7" in s):
        os.system("start photoshop")

    elif ("8" in s):
        os.system("start msedge")

    elif ("9" in s):
        os.system("start notepad")

    elif ("10" in s):
        os.system("start postman")

    else:
        pyttsx3.speak(s)
        print("The Command You Entered Is Invalid, Please Try Again")
        pyttsx3.speak("The Command You Entered Is Invalid, Please Try Again")

        

