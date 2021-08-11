
# ClipBoard History Logger 

import win32clipboard
import time


old = ""

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.ClosedClipboard()

    if old != data:
        with open("clip_history.txt", "w") as f:
            f.write(data + "\n")
        old = data

    time.sleep(0.6)

