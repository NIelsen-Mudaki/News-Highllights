class Config:

    news_api_base_url ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    
    pass



class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    
    DEBUG = True