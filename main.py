#Scrapping the ZOHO Website for internals and attendance marks. 3rd year CSE only!

from bs4 import BeautifulSoup
import urllib.request
import webbrowser

BASE_URL = 'https://creator.zohopublic.com/srm_university/attendance-2015-16/view-perma/Student_Status/H2rQs63qk22E9xdk1PAnBnNqzuFfgZMtD9yN5RkfuA7V6RsCdOfxxXeXjud80upTEZgQxjPJR3b0ffxU49rYOSr7fpaa9g1hRZmd/studentID=27276430000054'

def get_user_by_name(name):
    for i in range(79227,82151,4):
        x = urllib.request.urlopen(BASE_URL + str(i))
        soup = BeautifulSoup(x.read(),'html.parser')
        rows = soup.find("table",border=0).find_all('tr')
        col = rows[2].find_all('td')
        res = col[5].get_text()
        if(res == name):
            new = 2
            url = BASE_URL + str(i)
            webbrowser.open(url,new=new)
            return;
    print (name + '- Not found!')

def get_user_by_regno(regno):
    val = int(regno[7]+regno[8]+regno[9])
    flag = 0
    start_val = int(val*4 - 220)
    #79227 - 82151
    for i in range(79227+start_val,82151,4):
        print(i)
        x = urllib.request.urlopen(BASE_URL + str(i))
        soup = BeautifulSoup(x.read(),'html.parser')
        rows = soup.find("table",border=0).find_all('tr')
        col = rows[2].find_all('td')
        res = col[2].get_text()
        if(res > regno and flag == 0):
            i -= 24;
            flag = 1;
        elif(res == regno):
            new = 2
            url = BASE_URL + str(i)
            webbrowser.open(url,new=new)
            return;
    print (name + '- Not found!')
        
search =  int(input("How do you want to search? Register Number(1) or Name(2)?"))
if(search == 1):
    regno = str(input("Enter the Register Number:"))
    get_user_by_regno(regno);
else:
    name = str(input("Enter the name:"))
    get_user_by_name(name);
