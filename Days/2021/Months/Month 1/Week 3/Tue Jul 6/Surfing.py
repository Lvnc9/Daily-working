#! python3
# Start
# A train pashmaky file for doing some net stuff
# Modules
import webbrowser
import requests
import bs4
import selenium

#try:
#    responseObj = requests.get('https://shecan.ir/')
#    responseObj.raise_for_status()
#
#except Exception as exc:
#    print('The website Does not exist!\n [Error', responseObj.status_code + ']')
#
#else:
#    filehtml = open('./Daily/Days/Tue Jul 6/shecan.ir.html')
#
#    soupResponse = bs4.BeautifulSoup(filehtml, features='lxml')
#    selected_part = soupResponse.select('span')[0]
#    print(selected_part(''))

webbrowser.open('https://shecan.ir')
# End