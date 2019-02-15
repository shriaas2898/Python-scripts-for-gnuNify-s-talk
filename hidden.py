#!/bin/python
import os
for root,dirs,files in os.walk("/var/www/html"):
	for i in dirs:
		if(i[0] == "."):
			print i, "Directory"
	for j in files:
		if(j[0] == "."):
			print j, "File"

