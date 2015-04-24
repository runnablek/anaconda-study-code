import requests
import json
from BeautifulSoup import BeautifulSoup
from pymongo import MongoClient



def get_sector(soup):
    cominfo = soup.find('table', {'id':'comInfo'}).findAll('span', {'class':'exp'})[1].text[7:]
    return cominfo



def get_profit_per(soup):
   ss = soup.find('table', {'id':'cTB26'}).text
   return ss
   
    
    

def get_days_to_json(soup):
    script = soup.findAll('script')[4].string
    day = script.split("changeFin = ", 1)[1].split(";",1)[0]
    soup = BeautifulSoup(day)
    day = soup.text
    day = json.loads(day)    
    return day
    #print script


def get_data_to_json(soup):
    script = soup.findAll('script')[4].string
    data = script.split("changeFinData = ", 1)[1].split(";",1)[0]
    data = json.loads(data)    
    return data
    #print script    
    

    
code = '014530'

# page1
url = 'http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=' + code
r = requests.get(url)
soup1 = BeautifulSoup(r.text)

# page2
url = 'http://companyinfo.stock.naver.com/v1/company/cF1001.aspx?finGubun=MAIN&cmp_cd=' + code
r = requests.get(url)
soup2 = BeautifulSoup(r.text)



#print get_sector(soup1, code);
#print get_profit_per(soup2)

days = get_days_to_json(soup2)
data = get_data_to_json(soup2)


#print days

def set_json_data(dbas, day):
    for data1 in data:
        
        yy_dat = data1[0]    
        qt_dat = data1[1]
        
        for yy_dat1 in yy_dat:
            dnam = yy_dat1[0]
            for yy_dat2 in yy_dat1[1:]:
                jd = {"dbas": dbas, "dday": day, "dnam": dnam, "ddat": yy_dat2}
                posts.insert_one(jd).inserted_id
                                
        for qt_dat1 in qt_dat:
            for qt_dat2 in qt_dat1:
                #print dbas, day, dnam, qt_dat2
                jd = {"dbas": dbas, "dday": day, "dnam": dnam, "ddat": qt_dat2}
                iid =  posts.insert_one(jd).inserted_id
                print iid
                
    
  
    
    
    #for v in range(1,4):
        
        
client = MongoClient()
coinfo = client.test
posts = coinfo.posts


n = 0
for day1 in days:
    n = n + 1
    if n == 1:
        dbas = 'year'
    else:
        dbas = 'quarter'
    for day2 in day1:
       
        for data1 in data:
            #print dbas, day2
            set_json_data(dbas, day2)
            
            #post_id = posts.insert_one(jd).inserted_id
            #print post_id
            
        
    
    
 
 
















