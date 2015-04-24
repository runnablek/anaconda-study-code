import requests
import json
from BeautifulSoup import BeautifulSoup

def get_sector(code):
    url = 'http://finance.naver.com/item/main.nhn?code=' + code
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    
    sector = ""
    h4 = soup.find('h4', {'class':'h_sub sub_tit7'})
    if h4 is not None:
        sector = h4.a.text

    return sector



        
    
    

    
    
fn = 'data/krx_symbols.json'
with open(fn, 'r') as f:
    stock_list = json.load(f)


sector_list = []

# len(stock_list)
# test  :10
for s in stock_list[:10]:
    code = s['code'][1:]
    s['sector'] = get_sector(code)
    sector_list.append(s);
    #print s
    print s['full_code'], s['code'][1:], s['name'], s['sector']
    
    
j = json.dumps(sector_list)
with open('data/krx_sector.json', 'w') as f:
    f.write(j)    
    
    

fn = 'data/krx_sector.json'
with open(fn, 'r') as f:
    stock_list = json.load(f)

# len(stock_list)
for s in stock_list[:10]:
    print s['full_code'], s['code'][1:], s['name'], s['sector']

