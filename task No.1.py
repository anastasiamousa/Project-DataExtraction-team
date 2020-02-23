# - Taking the information stated at a table about the 7th semester courses at iee ihu department - 

#Importing BeautifulSoup library
Import requests
from bs4 import BeautifulSoup

#User agent header
header = { 
'User-Agent': 'Mozilla/5.0'
}

#Request 
page = requests.get('https://wwww.iee.ihu.gr/en/udg_courses/', headers=header)

soup = BeautifulSoup(page.content, 'html.parser')

#reach 7th semester table
tables = soup.find_all('table')
table = tables[6]
trs = table.find_all('tr')

#creating a list for contents
_7thInfo = list()
contents = ['code','course','category','theory-h','lab-h','ects']

#Loops through the table
for tr in trs:
  tds = tr.find_all('td')
  data = dict()
  
  for num,td in enumerate(tds): 
    

