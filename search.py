from bs4 import BeautifulSoup
import re 
import requests
import json

r = requests.get('http://boards.4chan.org/g/catalog#s=Desktop')

soup = BeautifulSoup(r.text)
script = soup.find('script',text=re.compile('.var.catalog.'))

json_text = re.search(r'.*var\s*catalog\s*=\s*({.*?});',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(1)

data = json.loads(json_text)


while True:

word=str(input("Enter search: "))

    for i in list(data['threads'].values()):
        text = i['teaser']
        if re.search(".*"+ word +".*",text)!=None:
            print(i['teaser'].encode('utf-8'))
            print("------------------------------------------------------------------------------------------------------")
