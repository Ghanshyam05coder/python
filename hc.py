import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show',])
profiles = [i.split(":")[1][1:-1] for i in data if "All U:"]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan'])
        results = [b.split(" : ")[1][1:-1] for b in results ]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

input("")        