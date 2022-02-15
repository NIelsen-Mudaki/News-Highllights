from flask import render_template
from . import main
from ..requests import get_source, news_source, get_headlines,get_category

# Views
@main.route('/')
def index():
    '''
        Root function with the home page
    '''

    source = get_source()
    headlines = get_headlines()

    return render_template('index.html', sources=source, headlines=headlines)


@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various news details page and its data
    '''
    
    news = news_source(id)
    return render_template('news.html',news = news,id=id )

@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'

    return render_template('categories.html',title = title,category = category)