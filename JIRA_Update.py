import requests
import json
import pyjq
import csv
import base64
import getpass

def JIRA_request(type, ticket, comment):
	url = "https://jira.atypon.com/rest/api/latest/"
	data = json.loads(r.text)
	data = d
	print(username)
	#print(username + " - " + str(data))
	return data


# Collect User Input
password = getpass.getpass(prompt="Enter JIRA credentials (username:password) ")
auth = "Basic " + base64.b64encode(password.encode("utf-8")).decode('ascii')


#Static Data
header = {"Content-Type":"application/json", "Authorization":auth}
