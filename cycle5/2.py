import requests
from bs4 import BeautifulSoup
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")
def getdata(url):
    r=requests.get(url)
    return r.content
htmldata = getdata("https://sjcetpalai.ac.in/")
#htmldata = getdata("https://sjcetpalai.ac.in/")
soup = BeautifulSoup(htmldata,'html.parser')
links = soup.find_all("a")
print("links:",len(links))
for link in links:
    if link.get("href") != "":
        print("Link:",link.get("href"),"Text", link.string)