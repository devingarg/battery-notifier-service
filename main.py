import psutil
from beepy import beep

# get the battery object
battery_obj = psutil.sensors_battery()

# retrieve battery charge
percent = battery_obj.percent

# retrieve plug status
plugged_in= battery_obj.power_plugged

if percent > 90 and plugged_in:
    beep(sound = 'ready')