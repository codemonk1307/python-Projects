
# run this script as root
import time
from datetime import datetime as dt 

# change hosts path according to your Operating System OS 
host_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"

# URL of websites which we want to block 
websites_list = list(input("Enter the URLs of Websites which you want to block separating them with spaces").split())
print("These are the websites which are going to be blocked on your Web Browser \n")
for count, websites in enumerate(websites_list, 1):
    print(count,":-", websites)

while True:
    # enter time of your work during which you want no distraction
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Your Working Hours are ....")
        with open(host_path, "r+") as file:
            content = file.read()
            for websites in websites_list:
                if websites in content:
                    pass
                else:
                    # mapping the hostnames to your localhost IP address
                    file.write(redirect + "" + websites + "\n")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(websites in line for websites in websites_list):
                    file.write(line)
        
        # removing the hostnames from the host file 
        file.truncate()
    print("Time for Fun Gaaaiizzz !!")

time.sleep(5)