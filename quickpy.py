from bs4 import BeautifulSoup
import requests
regno = '094'
html_text = requests.get('http://www.adhiyamaan.ac.in/anew/result1.php?regno=AC18UCS'+ regno + '&submit=submit').text
soup = BeautifulSoup(html_text, 'lxml')
string_content = soup.get_text()
print(string_content)
stringarray = string_content.split()
