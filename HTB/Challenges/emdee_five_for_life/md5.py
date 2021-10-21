import requests
import hashlib

url = 'http://165.22.121.146:30262/'
r = requests.session()
request = r.get(url)

html = request.text
start = "<h3 align='center'>"
end = "</h3><center>"

string = (html.split(start))[1].split(end)[0]

mdhash = hashlib.md5(str(string).encode('utf-8')).hexdigest()

data = dict(hash=mdhash)

response = r.post(url=url, data=data)

print(response.text)