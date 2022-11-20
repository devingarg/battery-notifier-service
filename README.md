# battery-notifier-service
A simple service to notify of a near-full battery level so you disconnect power on time


## About the files

The python script [main.py](main.py) contains the code that checks for the battery level and generates the audio notification.

Two libraries have been used for that:
* psutil
* beepy

They are present in the environment requirements file [req.txt](req.txt)

## 1. Setting up the python script

Create the virtual environment using [req.txt](req.txt).

Run the [main.py](main.py) file once, to test if things are going fine. (Modify the battery level check accordingly to test)

## 2. Creating the service

The service file can be renamed arbitrarily ([battery-notifier.service](battery-notifier.service)).

The following keys in the service file need to be set according to the user:
* `User`: the name of the user account on the machine
* `WorkingDirectory`: the root of the cloned repository because it is the location of the [main.py](main.py) file.
* `ExecStart`: the command used to start the program. Use the full python path to use the virtual env created above. Relative path of [main.py](main.py) is fine because we've set the working directory.

## 3. Starting the service

In order to start this file as a service, copy it to this location:
`/etc/systemd/system/`

Now, run the following command:
```bash
systemctl start battery-notifier
```

Note that if the service file is renamed, you'll have to put in the file's name here in place of `battery-notifier`.

**Note**: In order to set this service to start on boot, run the following:

```bash
systemctl enable battery-notifier
```

## 4. Some tweaks

Some options in the service file can be played around with:
* `RestartSec`: Sets the duration that the system waits once the program has executed to run it again. 

While writing more complex services, the keys like `After` become relevant because they help ensure pre-conditions are met before executing a service.