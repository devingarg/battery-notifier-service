import psutil
from beepy import beep

# get the battery object
battery_obj = psutil.sensors_battery()

# retrieve battery charge
percent = battery_obj.percent

# retrieve plug status
plugged_in= battery_obj.power_plugged

if plugged_in and percent > 87:
    beep(sound = 'ready')