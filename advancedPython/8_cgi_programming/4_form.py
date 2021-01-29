#!/usr/bin/env python3
import requests

url = "http://localhost/cgi-bin/cgi_programming/get_form.py"
first_name=input("Enter first name: ")
last_name=input("Enter last name: ")

data = {"first_name":first_name, "last_name":last_name}

print(requests.post(url, data).text)
