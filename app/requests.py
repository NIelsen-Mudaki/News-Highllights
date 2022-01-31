from app import app
import urllib.request,json

from app.views import news

News = news.News

# Getting api key
api_key = app.config['news_api_key']

base_url = app.config["news_api_base_url"]

def get_news(category):


    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results