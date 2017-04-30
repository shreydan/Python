"""
Written by: Shreyas Daniel - github.com/shreydan
Written on: 29 April 2017

Description: Prints project details of any kickstarter campaign.

Before executing:
    Please copy the URL of the project to project.txt (ONLY 1 URL at a time)
"""

import requests
from lxml import html
import os

def error_reason(issue):
    if issue == "empty file":
        print ("Please enter the correct URL of the kickstarter project in project.txt")
    else:
        print ("INVALID URL or NOT CONNECTED TO THE INTERNET.")

with open("project.txt","r") as project:
    file_size = os.stat("project.txt").st_size
    if file_size > 0:
        url = project.readline().rstrip()
    else:
        error_reason("empty file")
        exit()
    
try:
    project_page = requests.get(url)
except requests.exceptions.RequestException as e:
    error_reason(e)
    exit()

structure = html.fromstring(project_page.content)

creator = str(structure.xpath(".//*[@id='content-wrap']/section/div/div[2]/div/div/div[2]/span[1]/a/text()")[0]).strip()
title = str(structure.xpath(".//*[@id='content-wrap']/section/div/div[2]/div/div/div[3]/h2/text()")[0]).strip()
description = str(structure.xpath(".//*[@id='content-wrap']/section/div/div[2]/div/div/div[3]/p/text()")[0]).strip()
backers = str(structure.xpath(".//*[@id='backers_count']/text()")[0]).strip()
backed_amount = str(structure.xpath(".//*[@id='content-wrap']/section/div/div[1]/div[2]/div[1]/div[3]/div[1]/span[1]/text()")[0]).strip()
pledged_amount = str(structure.xpath(".//*[@id='content-wrap']/section/div/div[1]/div[2]/div[1]/div[3]/div[1]/span[3]/span[1]/text()")[0]).strip()

print ("CREATOR: "+creator)
print ("TITLE: "+title)
print ("DESCRIPTION: "+description)
print ("BACKED AMOUNT: "+backed_amount)
print ("PLEDGED AMOUNT: "+pledged_amount)

backed_amount = int(backed_amount[1:].replace(",",""))
pledged_amount = int(pledged_amount[1:].replace(",",""))
backed_percentage = str(int((backed_amount/pledged_amount)*100)) + "%"

print (backed_percentage + " FUNDED")
print ("BACKED BY: "+backers+" PEOPLE")
