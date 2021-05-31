import requests
import socket
from speedtest import Speedtest
from colorama import Fore, init
init()
print(Fore.RED+"                           _           _   ")
print(Fore.RED+"   _ __ ___   __ _     ___| |__   ___ | |_ ")
print(Fore.RED+"  | '_ ` _ \ / _` |   / __| '_ \ / _ \| __|")
print(Fore.RED+"  | | | | | | (_| |   \__ \ | | | (_) | |_ ")
print(Fore.RED+"  |_| |_| |_|\__, |___|___/_| |_|\___/ \__|")
print(Fore.RED+"             |___/_____|          V1       ")
print(Fore.YELLOW+f"\nGet Network Info")
print(Fore.YELLOW+f"Discord: mg_shot#8589")
print(Fore.BLUE+"App is started!\nWait a momnet")
st = Speedtest()
local_ip = socket.gethostbyname(socket.gethostname())
public_ip = requests.get("https://api.ipify.org").text
ip_loc = requests.get("https://api.iplocation.net/?ip="+public_ip).json()
name = (ip_loc['country_name'])
name_code = (ip_loc['country_code2'])

print(Fore.GREEN+'++++++++++++++++++++++++')
print(f"Local Ip: {local_ip}")
print('++++++++++++++++++++++++')
print(f"Public Ip: {public_ip}")
print('++++++++++++++++++++++++')
print(f"Country Name: ({name_code}):{name}")
print('++++++++++++++++++++++++')
print('Download Speed:', st.download(),)
print('++++++++++++++++++++++++')
print('Upload Speed:', st.upload())
print('++++++++++++++++++++++++')




