from zipfile import ZipFile
import string
import re

zip = "37366.zip"

done = 6

def strings(filename, min=4):
    with open(filename, errors="ignore") as f:  
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
        if len(result) >= min: 
            yield result

def unzip(f):
    s1 = list(strings(f))
    name = s1[-1].split('.')[0]
    if name is not None:
        print(name)
        with ZipFile(f) as zf:
            zf.extractall(pwd=name.encode())
        global zip
        zip = name + '.zip'
    else:
        done = 9
        print("YOU DID IT")

while True:
    unzip(zip)
    if done == 9:
        break
    