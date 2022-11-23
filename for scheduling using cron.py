from shutil import copy
import os


copy("./App.py", "/home")

path = "/var/spool/cron/crontabs"
if os.path.isfile(path):
    with open(path, "r+") as file:
        file.write("0 8 * * cd /home && sudo python3 App.py"+ "\n")
else:
    open(path, "x")
    with open(path, "r+") as file:
        file.write("0 8 * * cd /home && sudo python3 App.py"+ "\n")