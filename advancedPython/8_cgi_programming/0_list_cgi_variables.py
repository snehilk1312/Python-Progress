#!/usr/bin/env python3

import os
print("Content-type: text/html\r\n\r\n")
print("<font size+=1>Enviroment</font><\br>")
for param in os.environ.keys():
	print(f'<p>{param}: {os.environ[param]}</p> </br>')
