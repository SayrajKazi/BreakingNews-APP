from typing import Set
import requests as _requests
import bs4 as _bs4
import constants as _constants


def _create_url(tag: str) -> str:
    return f"https://www.bbc.com/news/{tag}"


def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup= _bs4.BeautifulSoup(page.content, "html.parser")

    return soup
""" 
def _extract_news_and_headlines(news):
    news_text =  news.content[0].strip()
#    // author = news.find(class_="nw-c-promo-meta").contents.strip()
    return news_text

# headlines = soup.find('body').find_all('h3') """



def scrape_news():
        collection = list()
        for tag in _constants.TAGS:
            url= _create_url(tag)
            soup = _get_page(url)
            x = soup.find('body').find_all('h3')
            
            for news in x:
                news_text= news.text.strip()
                data = {"News": news_text}
                collection.append(data)
        return collection



print(scrape_news())