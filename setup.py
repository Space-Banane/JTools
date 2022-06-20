import requests
import os

url = 'https://raw.githubusercontent.com/Space-Banane/JTools/main/JTools.py'
r = requests.get(url, allow_redirects=True)
username = os.getlogin()
os.mkdir("C:/Users/"+username+"/appdata/local/packages/pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0/localcache/local-packages/python39/site-packages/JTools/")
open('C:/Users/'+username+"/appdata/local/packages/pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0/localcache/local-packages/python39/site-packages/JTools/JTools.py", 'wb').write(r.content)
print("Done")