#automatic ConfigurationChangingReporter

Use the script to send yourself an email with the (changed/added/deleted) configuration on your cisco switch

use the second script to assigning a cron task automatically to send yourself an email on a regular basis

1st script APP.py does the follwoing

1-The script uses the Netmiko and ConnectHandler libraries from the netmiko package to establish an SSH connection to the device with the specified IP address and username/password credentials. It then sends the sh ru command to the device to retrieve its current configuration.

2-The script then saves the current configuration to a file with the format configFiles/<device IP>_<current date>. The previous day's configuration is read from a file with the same format but with the date being one day less than the current date.

3-The script uses the difflib library to compare the two configurations and create an HTML file that highlights the differences between the two configurations.

4-The script then uses the smtplib library to connect to an email server, login using the specified email address and password, and send an email with the subject "Daily configuration difference report." The email contains the HTML file with the highlighted differences as an attachment.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
The 2nd script will create a cron job that will run the App.py script every day at 8:00 AM by doing the Following:

1-Imports the copy function from the shutil module to copy a file App.py to the /home directory.

2-Imports the os module and sets the value of path to the location of the crontab file, "/var/spool/cron/crontabs".

3-The code checks if the file exists at the path and,
  *If the file exists, it opens the file in "r+" (read and write) mode and writes the following line to the file: "0 8 * * cd /home && sudo python3 App.py"
  *If the file does not exist, it creates a new file using the "x" (exclusive creation) flag and writes the same line of text to the file as mentioned above.


