
# parsing the HTML content 
# online ide will not support this -----
import requests 
from bs4 import BeautifulSoup

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

# if below mentioned code generates an error .... run ("pip install html5lib")  or  (install html5lib)
soup = BeautifulSoup(r.content, "html5lib")
print(soup.prettify())