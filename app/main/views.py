from flask import render_template
from . import main
from ..requests import get_source, article_source, get_headlines,get_category

# Views
@main.route('/')
def index():
    '''
        Root function with the home page
    '''

    source = get_source()
    headlines = get_headlines()

    return render_template('index.html', sources=source, headlines=headlines)


@main.route('/articles/<id>')
def news(id):

    '''
    View article page function that returns the various news details page and its data
    '''
    
    articles = article_source(id)
    return render_template('article.html',articles = articles,id=id)

@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the category.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'

    return render_template('category.html',title = title,category = category)