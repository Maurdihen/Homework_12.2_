from flask import Blueprint, render_template, request
from functions import search_content
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)\

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def main_page():
    logging.info('Открывал главную страницу')
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    post = search_content(s)
    logging.info('Выполнял поиск')
    return render_template('post_list.html', post=post, s=s)