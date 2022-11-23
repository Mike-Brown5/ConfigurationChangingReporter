import difflib, datetime, smtplib 
from netmiko import Netmiko, ConnectHandler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#IP address for the main device
ip = "192.168.104.120"

# Assigning the device type for netmiko custtomization
device_type = "arista_eos"

user_name= "admin"
pasword = "admin"

command = "sh ru"

# using SSH session to connect
print("connecting to the switch.......")
session = ConnectHandler(device_type=device_type,ip= ip, username=user_name,password = pasword,global_delay_factor=5)

#accesing the enable terrminal
enable =session.enable()


print("sending commands.......")
output = session.send_command(command,read_timeout=15)


deviceOldConfig = "configFiles/" + ip + '_' + (datetime.date.today() - datetime.timedelta(days = 1)).isoformat()

currentConfig = "configFiles/" + ip + '_' + datetime.date.today().isoformat()
print("Writing down the runnig config.......")
with open(currentConfig,'w') as newConfig:
    newConfig.write(output + "\n")
print("comparing and highliting the diffrent configs.......")
with open(deviceOldConfig,'r') as oldFile ,open(currentConfig,'r') as newFile:
    diff = difflib.HtmlDiff().make_file(fromlines = oldFile.readlines(), tolines=newFile.readlines(), fromdesc="Yesterday", todesc="Todaay")

print("connecting to protonmail server.......")
mail = "Your outook email" ######REPLACE!!!!!!!!!!!!!
pas = "your password" ######REPLACE!!!!!!!!!!!!!

server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
server.connect("smtp-mail.outlook.com", port=587)
server.ehlo()
server.starttls()
server.ehlo()
print("logining in.......")
server.login(user=mail, password=pas)


print("sending the Email.....")
message = MIMEMultipart()
message['From'] = mail
message['To'] = mail
message['Subject'] = "Daily configration diffrence report"

message.attach(MIMEText(diff,'html'))
server.sendmail(from_addr=mail, to_addrs=mail ,msg=message.as_string())
server.quit()
