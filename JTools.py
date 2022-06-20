import json
"""
JTools
~~~~~~~~~~~~~~~~~~~

FUNCTIONS :
-Read()
-Write()


https://github.com/Bigboi-Python/JTools

This is a wrapper of the json module(this is easyer to use)


JTools 2022 June 
"""

def Save(data,file):
    with open(file,"w") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

def Read(file):
    with open(file,"r") as f:
        data = json.load(f)
        print(data)