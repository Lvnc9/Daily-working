#! python3
# Start
# Will biggin with the chapter 11 and web scripting and do some pashmaki easy web scripting
# Modules
import webbrowser
import requests
import os
import bs4

try:
    info = requests.get('https://en.wikipedia.org')
    info.raise_for_status()
    into = open('./Daily/Days/Sun Jul 4/example.html')
except Exception as exc:
    print('The Web page does not exist!')
    
else:
    intosoup = bs4.BeautifulSoup(into, features='lxml')
    spanElem = intosoup.select('span')[0]
    print(str(spanElem))
    print(spanElem.get('id'))``
    print(spanElem.get('somepashmakfalse') == None)
    print(spanElem.attrs)
# End