
# installing required libraries
# pip install requests 
# pip install html5lib 
# pip install bs4

# accessing the HTML content from webpage
import requests 
URL = "https://www.codechef.com/problems/school/?itm_medium=navmenu&itm_campaign=problems"
r = requests.get(URL)
print(r.content)


