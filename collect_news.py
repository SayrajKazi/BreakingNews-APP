import json as _json

import scraper as _scraper


if __name__ == "__main__":
    news = _scraper.scrape_news()
    with open("news.json", mode= "w") as news_file:
        _json.dump(news, news_file, ensure_ascii=False)

