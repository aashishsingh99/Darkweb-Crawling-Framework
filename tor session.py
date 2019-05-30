import requests
session=requests.session()
session.proxies={}

r = session.get("http://httpbin.org/ip")
print("original ip")
print(r.text)

session.proxies['http'] = 'socks5h://localhost:9150'
session.proxies['https'] = 'socks5h://localhost:9150'
r = session.get("http://httpbin.org/ip")
print("after connected to tor")
print(r.text)

r = session.get("https://www.facebookcorewwwi.onion/")
print(r.headers)