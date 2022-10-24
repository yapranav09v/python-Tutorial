#using a json module
#importing a json module
#Full form of json :- javascript object notation
import json

data = '{"var1":"harry", "var2":56 }'

#Using a loads functio to load data with respect to json
parsed = json.loads(data)
#we used it because with that we can use thise as key value pair to
print(parsed['var1'])
print(type(parsed))

#Using a load
data2 = {
    "channel_name": "codeWithHaryy",
     "cars": ['bmw', 'audi a8', 'ferrari' ], 
    "fridge": ('roti', 540),
    "isbad": False
}
#dump will give javascript compatable object
# for example the False is in javascript is like false f is small in js 
jscomp = json.dumps(data2)
print(jscomp)