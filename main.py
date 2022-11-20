import psutil
from beepy import beep

# get the battery object
battery_obj = psutil.sensors_battery()

# check for battery percent
percent = battery_obj.percent

if percent > 40:
    beep(sound = 'ready')