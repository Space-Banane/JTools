"""
JTools
~~~~~~~~~~~~~~~~~~~

FUNCTIONS :
-Read(file)
-Save(data,file)
-load(data,file)


https://github.com/Space-Banane/JTools

This is a wrapper of the json module(this is easyer to use)


JTools 2022 June 
"""
import json

def Save(data,file):
    with open(file,"w") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

def Read(file):
    with open(file,"r") as f:
        data = json.load(f)
        print(data)

def load(data,file):
    with open(file,"r") as f:
        loaded = json.load(f)
        data = loaded[data]
        return data

def loadfile(file):
    with open(file,"r") as f:
        data = json.load(f)
        return data