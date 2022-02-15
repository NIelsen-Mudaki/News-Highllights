from .models import NewsSource, News
import urllib.request,json

def configure_request(app):
    global api_key, source_url, category_url
    api_key = app.config['NEWS_API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    category_url=app.config['CATEGORY_API_URL']


def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = NewsSource(id,name,description,url)
            source_results.append(source_object)

    return source_results

def news_source(id):
    news_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(news_source_url)
    with urllib.request.urlopen(news_source_url) as url:
        news_source_data = url.read()
        news_source_response = json.loads(news_source_data)

        news_source_results = None

        if news_source_response['articles']:
            news_source_list = news_source_response['articles']
            news_source_results = process_news_results(news_source_list)
    
    return news_source_results

def process_news_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    news_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            news_objects = News(author,description,time,image,url,title)
            news_source_results.append(news_objects)

    return news_source_results