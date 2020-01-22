import requests
import json
import pyjq
import csv
import base64
import getpass

def JIRA_request(update_type, ticket, parameter):
	url = "https://jira.atypon.com/rest/api/latest/" + ticket
	if update_type = "comment":
		url += "/comment"
		d = {"body": parameter}
	elif update_type = "assign":
		url += "/assignee"
		d = {"name": parameter}
	r = requests.get(url, headers = header, data = d)
	request_text = dump.dump_all(r)
	print(request_text)

# Collect User Input
password = getpass.getpass(prompt="Enter JIRA credentials (username:password) ")
auth = "Basic " + base64.b64encode(password.encode("utf-8")).decode('ascii')

#Static Data
header = {"Content-Type":"application/json", "Authorization":auth}

#initiate
with open('tickets.csv') as csv_file:
	fieldnames = ['type', 'ticket', 'parameter']
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    	for row in csv_reader:
    			print(row['ticket'])
    			JIRA_request(row["type"], row['ticket'], row["parameter"])
