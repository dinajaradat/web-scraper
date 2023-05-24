import requests
from bs4 import BeautifulSoup
def get_citations_needed_count(url):
    page = requests.get(url)
    # return page.content
    soup = BeautifulSoup(page.content , 'html.parser')
    # return soup
    passages = soup.find_all('sup', class_ = 'noprint Inline-Template Template-Fact')

    return (len(passages))

def get_citations_needed_report(url):
    page = requests.get(url)
    # return page.content
    soup = BeautifulSoup(page.content , 'html.parser')
    # return soup
    passages = soup.find_all('p')

    p_List = []
    for passage in passages:
        find_p =  passage.find('sup' , class_ ='noprint Inline-Template Template-Fact')
        if find_p:

           p_List.append(passage.text)
        
    print ('\n'.join(p_List))


url = "https://en.wikipedia.org/wiki/History_of_Mexico"
print(get_citations_needed_count(url))
print(get_citations_needed_report(url))