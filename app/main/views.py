from flask import render_template
from . import main
from ..requests import get_source, news_source

# Views
@main.route('/')
def index():
    '''
        Root function with the home page
    '''

    source = get_source()

    return render_template('index.html', sources=source)


@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various news details page and its data
    '''
    
    news = news_source(id)
    return render_template('news.html',news = news,id=id )