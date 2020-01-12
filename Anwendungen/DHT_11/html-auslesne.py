class AppURLopener(urllib.reques.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('<192.168.178.190>')

for line in response:
    print(line)