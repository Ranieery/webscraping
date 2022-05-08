
import requests
from bs4 import BeautifulSoup

url = 'https://moz.com/top500'
page = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('table', class_='table table-responsive-md table-bordered table-zebra mb-0 table-sticky').text)

