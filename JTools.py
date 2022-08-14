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
    try:
        with open(file,"w") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
    except:
        raise Exception("Could not save Data to file")

def Read(file):
    try:
        with open(file,"r") as f:
            data = json.load(f)
            return (data)
    except:
        raise Exception("Could not return Data from file")

def load(data,file):
    try:
        with open(file,"r") as f:
            loaded = json.load(f)
            data = loaded[data]
            return data
    except:
        raise Exception("Could not load Data from file")

