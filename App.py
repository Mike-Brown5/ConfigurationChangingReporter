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

enable =session.enable()

output = session.send_command(command)

deviceOldConfig = "configFiles/" + "_" + ip + (datetime.date().today() - datetime.timedelta(days=1)).isoformat()

currentConfig = "configFiles/" + ip + datetime.date().today().isoformat()

with open(currentConfig,'w') as newConfig:
    newConfig.write(output + "\n")

with open(deviceOldConfig,'r') as oldFile ,open(currentConfig,'r') as newFile:
    diff = difflib.HtmlDiff().make_file(fromlines = oldFile.readlines(), tolines=newFile.readlines(), fromdesc="Yesterday", todesc="Todaay")

fromE = "mike505brown@gmail.com"
toE = "mike505brown@gmail.com"

message = MIMEMultipart()
message['From'] = fromE
message['To'] = toE
message['Subject'] = "Daily configration diffrence report"

message.attach(MIMEText(diff,'html'))
# sending email via gmail server using port 587
server = smtplib.SMTP('smtp.gmail.com',587)

# encrypting all smtp commands
server.starttls()

server.login(mike505brown, Mike55555)

server.sendmail(fromE, toE, message.as_string())
server.quit()