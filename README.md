# JTools
JTools is a Wrapper of json(python module)


Example:
good
```
import JTools

data = {
    "name" : None,
    "beans": 1
}

JTools.Save(data,"memberbeans.json")
```
bad
```
import json

data = {
    "name" : None,
    "beans": 1
}

with open("memberbeans.json","w") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

```
