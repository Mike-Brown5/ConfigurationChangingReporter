import difflib, datetime, smtplib
from netmiko import ConnectHandler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#IP address for the device
ip = "192.168.104.120"

# Assigning the device type for netmiko custtomization
device_type = "arista_eos"

user_name= "admin"
pasword = "admin"

command = "sh ru"

# using SSH session to connect
session = ConnectHandler(device_type=device_type,ip= ip, username=user_name,password = pasword,global_delay_factor=4)

output = session.send_command(command)
