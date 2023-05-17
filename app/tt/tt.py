import pandas as pd
import requests

remote_files = "http://vps36332.publiccloud.com.br/static/files.json" 

req = requests.get(remote_files)
print(req.status_code)
print(req.encoding)
print(req.text)
print(req.json())

remote_url = "http://vps36332.publiccloud.com.br/static/UFCA_2022_11.csv.zip"


#data = pd.read_csv(remote_url, low_memory=False, encoding="UTF-16", sep=";")
#print(data)

