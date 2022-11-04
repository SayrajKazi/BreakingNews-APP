from typing import Dict, List
import json as _json
import random as _random


def _get_headlines() -> List :
    with open("news.json") as news_file:
        news = _json.load(news_file)
    
    return news


def _get_random_news() -> Dict:
    headlines = _get_headlines()
    headline = _random.choice(headlines)

    return headline

def _form_tweet(news: Dict[str, str]) -> str:
    tweet = f"{news['News']}" 

    return tweet

def _is_valid_characters(tweet: str) -> bool:
    return len(tweet) <= 280


def get_tweet():
    while True:
        headline = _get_random_news()
        tweet = _form_tweet(headline)
        if _is_valid_characters(tweet):
            return tweet
    

print(get_tweet())
