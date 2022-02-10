from flask import render_template
from . import main
from ..requests import get_source

# Views
@main.route('/')
def index():
    '''
        Root function with the home page
    '''

    source = get_source()

    return render_template('index.html', sources=source)


@main.route('/news/<int:news_id>')
def news(news_id):
    

    return render_template('news.html')