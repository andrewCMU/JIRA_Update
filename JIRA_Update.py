import requests
from requests_toolbelt.utils import dump
import json
import pyjq
import csv
import base64
import getpass
import re

def comment(update_type, ticket, parameter):
	url = base_url + ticket + "/comment"
	d = {"body":str(parameter)}
	r = requests.post(url, headers = header, data = json.dumps(d))
	response(r)

def assign(update_type, ticket, parameter):
	url = base_url + ticket + "/assignee"
	d = {"name":str(parameter)}
	r = requests.put(url, headers = header, data = json.dumps(d))
	response(r)

def response(r):
	#print(r.content)
	if(pattern.match(str(r.status_code))):
		print("Succesfull Update")
	else:
		print("Failed Update: Error " + str(r.status_code))
	pass

# Collect User Input
print("Welcome to the JIRA Update Ticket. Please ensure you are connected to your VPN before continuing")
password = getpass.getpass(prompt="Enter your JIRA credentials (username:password): ")
auth = "Basic " + base64.b64encode(password.encode("utf-8")).decode('ascii')

#Static Data
header = {"Content-Type":"application/json", "Authorization":auth}
base_url = "https://jira.atypon.com/rest/api/latest/issue/"
pattern = re.compile('^20\d')

#initiate
with open('tickets.tsv') as tsv_file:
	fieldnames = ['type', 'ticket', 'parameter']
	tsv_reader = csv.DictReader(tsv_file, dialect='excel-tab', fieldnames=fieldnames)
	for row in tsv_reader:
			print("****\n" +row['ticket'])
			if (row["type"] == "comment"):
				comment(row["type"], row['ticket'], row["parameter"])
			elif (row["type"] == "assign"):
				assign(row["type"], row['ticket'], row["parameter"])
			else:
				print("Invalid Update Type")
