from shutil import copyfile

copyfile("./App.py", "/home")

path = "/var/spool/cron/crontabs"

with open(path, "r+") as file:
    file.write("0 8 * * cd /home && sudo python3 App.py"+ "\n")