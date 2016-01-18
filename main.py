#Scraping the ZOHO Website for internals and attendance marks. 3rd year CSE only(2013-2017 batch)!

from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib.request
import webbrowser

BASE_URL = 'https://creator.zohopublic.com/srm_university/attendance-2015-16/view-perma/Student_Status/H2rQs63qk22E9xdk1PAnBnNqzuFfgZMtD9yN5RkfuA7V6RsCdOfxxXeXjud80upTEZgQxjPJR3b0ffxU49rYOSr7fpaa9g1hRZmd/studentID=27276430000054'

#Creating Connection
try:
    con = MongoClient()
    db = con['zohodb']
    stdColl = db.stdColl
except:
    print ("[Error] Could not connect with mongodb. Try again.")

#Main Scraper
def main_scraper():
    #for person in db.stdColl.find():
     #   stdColl.remove(person)
    #79227 - 82151
    for i in range(79227,82152,4):
        student = {}
        url = urllib.request.urlopen(BASE_URL + str(i))
        soup = BeautifulSoup(url.read(), 'html.parser')
        rows = soup.find("table",border=0).find_all('tr')
        col = rows[2].find_all('td')
        regID = str(col[2].get_text())
        name = str(col[5].get_text())
        student['_id'] = regID
        student['url'] = str(i)
        student['name'] = name
        print (student)
        stdColl.insert(student)
    return;

#Search by name
def get_user_by_name(name):
    try:
        student = db.stdColl.find_one({'name' : name})
        new = 2
        stdURL = BASE_URL + str(student['url']);
        webbrowser.open(stdURL, new=new)
        return;
    except:
        print ('[ERROR]' + name + ' not found.')

#Search by Register Number
def get_user_by_regno(regno):
    try:
        student = db.stdColl.find_one({'_id' : regno})
        new = 2
        stdURL = BASE_URL + str(student['url']);
        webbrowser.open(stdURL, new=new)
        return;
    except:
        print ('[ERROR]' + regno + ' not found.')

#Main scraper
#Uncomment the line below, create the database, access all the records in O(1).
#main_scraper();

#I/O
search =  int(input("How do you want to search? Register Number(1) or Name(2)? "))
if(search == 1):
    regno = str(input("Enter the Register Number: "))
    get_user_by_regno(regno);
else:
   name = str(input("Enter the name: "))
   get_user_by_name(name);
