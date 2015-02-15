import requests
import json
from BeautifulSoup import BeautifulSoup



url = 'http://www.krx.co.kr/por_kor/popup/JHPKOR13008.jsp'
r = requests.post(url, data={'mkt_typ':'S', 'market_gubun': 'allVal'})

soup = BeautifulSoup(r.text)
table = soup.find('table', {'id':'tbl1'})
trs = table.findAll('tr')

stock_list = []

for tr in trs[1:]:
    stock = {}
    cols = tr.findAll('td')
    stock['code'] = cols[0].text[0:]
    stock['name'] = cols[1].text.replace(";", "")
    stock['full_code'] = cols[2].text
    stock_list.append(stock)
    
    
j = json.dumps(stock_list)
with open('data/krx_symbols.json', 'w') as f:
    f.write(j)
    
    
fn = 'data/krx_symbols.json'
with open(fn, 'r') as f:
    stock_list = json.load(f)

# len(stock_list)
for s in stock_list[:10]:
    print s['full_code'], s['code'][1:], s['name']
    
    