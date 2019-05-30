from collections import deque
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import requests

session=requests.session()
session.proxies={}


session.proxies['http'] = 'socks5h://localhost:9150'

session.proxies['https'] = 'socks5h://localhost:9150'

url="http://facebookcorewwwi.onion"

b = session.get(url)

print ("Page to be crawled:", url)


queue = deque([])

visited_list = []

def crawl(url):
    visited_list.append(url)
    if len(queue) > 99:
        return

   # urlfg=session.get("http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q=cyber&cmd=Search%21")
    #urlf = urllib.request.urlopen(b)
    #urlf=session.urlopen(url)
    #print("\n\n\n\n")
    #print(urlf)
    
    soup = BeautifulSoup(b.content)
    urls = soup.findAll("a", href=True)
    #urls = soup.findAll("a href^=http://www.mkyong.com/page/")

    for i in urls:
        flag = 0
        
        complete_url = urljoin(url, i["href"]).rstrip('/')

        
        for j in queue:
            if j == complete_url:
                flag = 1
                break

        
        if flag == 0:
            if len(queue) > 99:
                return
            if (visited_list.count(complete_url)) == 0:
                queue.append(complete_url)

    
    current = queue.popleft()
    crawl(current)

crawl(url)

#print queue
for i in queue:
    print(i)
    print("\n\n-----")
    r = session.get(i)
    text=r.content

    html=text
    soup=BeautifulSoup(html,"html5lib")
    type(soup)
    print(soup.title)
    

with open(r'C:\Users\Aashish Singh\Desktop\webcrawl\crawled.txt', 'w') as f:
    for item in queue:
        f.write("%s\n" % item)

print ("Pages crawled:")

