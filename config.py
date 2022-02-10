import os

class Config:

    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'

    CATEGORY_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    
    pass



class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}