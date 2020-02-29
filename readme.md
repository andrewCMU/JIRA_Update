# Atypon JIRA Update Tool
The purpose of this tool is to allow for bulk updates to JIRA tickets using a tsv file

## Getting Started

This tool is meant to be used with Python 3. The following libraries will also need to be installed
- requests
- pyjq
- getpass

Other libraries should be standard

## Using the tool

The TSV takes in 3 parameters
- What you would like to do with the ticket(comment, assign, resolve, close))
- Ticket number
- Data parameter

The Data parameter varies depending on the ticket type
- Comment: comment to be added
- Assign: user code for assignment
- Resolve: Resolution Type
- Close: Resolution Type

You must enter one of the following resolution types in order for the program to continue
- Fixed
- Won't Fix
- Duplicate
- Incomplete
- Cannot Reproduce
- Invalid
- Later
- Remind
- Moved
- Done
- Wrongly Reopened
- Won't Do