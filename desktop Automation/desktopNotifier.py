

# python -m pip install win10toast
from win10toast import ToastNotifier

# One-time initialization
toaster = ToastNotifier()

# display the notifications whenever needed
toaster.show_toast("New Notification!", "Alert! Yes", threaded = True, icon_path = None, duration = 3) # 3 seconds


# to check if any notifications are active we use "toaster.notification_active()"
import time

while toaster.notification_active():
    time.sleep(0.1)

    