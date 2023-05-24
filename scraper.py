import requests
from bs4 import BeautifulSoup
def get_citations_needed_count(url):
    page = requests.get(url)
    # return page.content
    soup = BeautifulSoup(page.content , 'html.parser')
    # return soup
    passages = soup.find_all('div',class_ = 'mw-body-content mw-content-ltr')

    passage_List = []
    citations = 0
    for passage in passages:
        find_citations = passage.find('sup' , class_ ='reference').text
        if find_citations == "[citation needed]":
          citations += 1
          passage_List.append(find_citations)
    print (passage_List)

def get_citations_needed_report(url):
    page = requests.get(url)
    # return page.content
    soup = BeautifulSoup(page.content , 'html.parser')
    # return soup
    passages = soup.find_all('div',class_ = 'mw-body-content mw-content-ltr')

    p_List = []
    for passage in passages:
        find_p =  passage.find('p' , class_ ='').text
        find_citations = passage.find('sup' , class_ ='reference').text
        if find_citations == "[citation needed]":
         
          p_List.append(find_citations)
        
    print (p_List)


url = "https://en.wikipedia.org/wiki/History_of_Mexico"
print(get_citations_needed_count(url))