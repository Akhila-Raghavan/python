import requests
import re
from bs4 import BeautifulSoup


url = 'https://ful.io'
req = requests.get(url)
soup = BeautifulSoup(req.text,'html.parser')
urls =[]
s=[]
index=0
for link in soup.find_all('a'):
    urls.append(link.get('href'))



while index < len(urls):
    char = urls[index]
    if char[0:4] =='http':


        s.append(char)
    index +=1
print(s)
print(urls)
print('Emails:')
#pattern =re.compile( r'[a-zA-Z0-9\.]+@[a-zA-Z\.]*\.io')
pattern = r'[\w\.-]+@[\w\.-]+'
r=requests.get(url)

for  match in re.findall(pattern,r.text):
    print(match)


print('contactUS')
c=[]
index=0
while index < len(urls):
    char = urls[index]
    if char[0:3] =='tel':


        c.append(char)
    index +=1
print(c)
