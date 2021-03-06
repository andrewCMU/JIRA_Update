import requests
from requests_toolbelt.utils import dump
import json
import pyjq
import csv
import base64
import getpass
import re
import keyring
import sys

def comment(ticket, parameter):
	url = base_url + ticket + "/comment"
	d = {"body":str(parameter)}
	r = requests.post(url, headers = header, data = json.dumps(d))
	response(r)

def assign(ticket, parameter):
	url = base_url + ticket + "/assignee"
	d = {"name":str(parameter)}
	r = requests.put(url, headers = header, data = json.dumps(d))
	response(r)

def resolve(ticket, parameter):
	resolution = get_resolution(parameter)
	if resolution == "Invalid":
		print("Invalid Resolution, no update to be preformed")
		pass
	url = base_url + ticket + "/transitions"
	d = {"fields": {"resolution": {"name": resolution}},"transition": {"id": "5"}}
	r = requests.post(url, headers = header, data = json.dumps(d))
	response(r)

def close(ticket, parameter):
	resolution = get_resolution(parameter)
	if resolution == "Invalid":
		print("Invalid Resolution, no update to be preformed")
		pass
	url = base_url + ticket + "/transitions"
	d = {"fields": {"resolution": {"name": resolution}},"transition": {"id": "702"}}
	r = requests.post(url, headers = header, data = json.dumps(d))
	response(r)

def response(r):
	#print(r.content)
	if(pattern.match(str(r.status_code))):
		print("Status " + str(r.status_code) + " Succesfull Update")
	else:
		print("Failed Update: Error " + str(r.status_code))
		print(r.json())

def get_resolution(text):
	resolutions = ["Fixed","Won't Fix","Duplicate","Incomplete","Cannot Reproduce","Invalid","Later","Remind","Moved","Done","Wrongly Reopened","Won't Do"]
	res_lower = [item.lower() for item in resolutions]
	res_index = res_lower.index(text.lower())
	return resolutions[res_index]

# Collect User Input
print("Welcome to the JIRA Update Ticket. Please ensure you are connected to your VPN before continuing")
# Password input can be done in a variety of ways. Comment out the keyring lines uncomment the getpass lines to enter the password manually each time.
username = "aschwartz"
password =  keyring.get_password("Python_JIRA","aschwartz")
auth = "Basic " + base64.b64encode((username + ":" +password).encode("utf-8")).decode('ascii')
#password = getpass.getpass(prompt="Enter  your JIRA credentials (username:password): ")
#auth = "Basic " + base64.b64encode(password.encode("utf-8")).decode('ascii')

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
				comment(row['ticket'], row["parameter"])
			elif (row["type"] == "assign"):
				assign(, row['ticket'], row["parameter"])
			elif (row["type"] == "resolve"):
				resolve(, row['ticket'], row["parameter"])
			elif (row["type"] == "close"):
				close(row["type"], row['ticket'], row["parameter"])
			else:
				print("Invalid Update Type")
