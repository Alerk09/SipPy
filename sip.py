from plyer import notification
import random
import time
import getpass
import os
import platform
import pystray
import threading
from PIL import Image
user = getpass.getuser()

# Customize to your liking.
titles = ["Time to Hydrate!", "H2O Alert!", "NO WATER?", "Hydration Break", "Water Time!", "Liquid Recharge", f"{user}! Stay hydrated...", "Fuel up!", "Aqua Break!"]
messages = ["Drink water to stay healthy.", "Your body says it’s thirsty.. drink some water!", "I know you are thirsty, take a sip!", "Time to give your cells a drink.", "Fuel up with a refreshing sip."]
delay = 745
display_time = 5

# Detects OS and uses the correct icon image format.
if platform.system() == "Windows":
    osicon = "sippy.ico"
else:
    osicon = "sippy.png"
iconpath = os.path.abspath(os.path.join(os.path.dirname(__file__), osicon))
trayicon = Image.open(iconpath)

# Checks if paused, then chooses a title and a description, and notifies using both of them.
def hydrate(): 
       while True:
         if not paused:
           rantl = random.choice(titles)
           ranmsg = random.choice(messages)
           notification.notify(title=rantl, message=ranmsg, timeout=display_time, app_name="SipPy", app_icon=iconpath)
           time.sleep(delay)

# Makes a tray for easy access.
paused = False
def pause_resume(icon, item):
    global paused
    paused = not paused
def prdetect(item):
    return "Pause" if not paused else "Resume"
def quit_app(icon,item):
    icon.stop()

tray = pystray.Icon("SipPy", icon=trayicon, menu=pystray.Menu(pystray.MenuItem(prdetect, pause_resume), pystray.MenuItem("Quit", quit_app)))

# Runs the hydrate function in the background and the tray.
threading.Thread(target=hydrate, daemon=True).start()
tray.run()



