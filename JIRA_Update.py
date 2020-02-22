import requests
from requests_toolbelt.utils import dump
import json
import pyjq
import csv
import base64
import getpass

def JIRA_request(update_type, ticket, parameter):
	url = "https://jira.atypon.com/rest/api/latest/issue/" + ticket
	if update_type == "comment":
		url += "/comment"
		d = {"body":str(parameter)}
		r = requests.post(url, headers = header, data = json.dumps(d))
	elif update_type == "assign":
		url += "/assignee"
		d = {"name":str(parameter)}
		r = requests.put(url, headers = header, data = json.dumps(d))
	
	request_text = dump.dump_all(r)
	print(request_text)

# Collect User Input
password = getpass.getpass(prompt="Enter JIRA credentials (username:password) ")
auth = "Basic " + base64.b64encode(password.encode("utf-8")).decode('ascii')

#Static Data
header = {"Content-Type":"application/json", "Authorization":auth}

#initiate
with open('tickets.tsv') as tsv_file:
	fieldnames = ['type', 'ticket', 'parameter']
	tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab', fieldnames=fieldnames)
	for row in tsv_reader:
			print(row['ticket'])
			JIRA_request(row["type"], row['ticket'], row["parameter"])
