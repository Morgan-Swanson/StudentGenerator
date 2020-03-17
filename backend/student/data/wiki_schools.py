import wikipedia
from bs4 import BeautifulSoup
html = wikipedia.page("List of high schools in California").html()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
