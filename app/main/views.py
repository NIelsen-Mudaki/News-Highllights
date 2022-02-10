from flask import render_template
from app import app
from ..requests import get_news

# Views
@app.route('/')
def index():

    top_headlines = get_news('headlines')

    return render_template('index.html', headlines = top_headlines)


@app.route('/news/<int:news_id>')
def news(news_id):
    

    return render_template('news.html')