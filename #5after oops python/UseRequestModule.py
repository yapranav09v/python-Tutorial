#use of request module in python
#imprting requests module
import requests

#declaring and getting a request from http url
r = requests.get("https://requests.readthedocs.io/en/latest/")
print(r.text) #printing a text from requests which is html code because of random url

url = "www.somthing.com"
data = {
    "p1": 4,
    "p2": 8,
}
r2 = requests.post(url = url, data = data)

#For more informaiton you can serch it on a documentation of requests module and for your future work








