
# You need to provide a (txt) file consisting the WIFI Passwords and 
# save it to the same location where you are running your code 
# or provide the right path of that file 

import subprocess

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print(profiles)

result_file = open("results.txt", "w")

for i in profiles:
    results = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key = clear"]).decode("utf-8").split("\n")
    results = [d.split(":")[1][1:-1] for d in results if "Key Content" in d]

    try:
        print("{:<30}| {:<}".format(i, results[0]))
        result_file.write("{:<30}| {:<}\n".format(i, results[0]))
    except IndexError:
        print("")
