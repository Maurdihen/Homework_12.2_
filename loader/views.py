from flask import Blueprint, render_template, request
from functions import new_post
import logging

# logger = logging.getLogger('logger_louder')
# file_logger = logging.FileHandler('logger_louder.log')
# formater_logger = logging.Formatter('%(asctime)s : %(message)s : %(pathname)s : %(funcName)s : &(levelname)s')
# logger.addHandler(file_logger)
logging.basicConfig(filename='basic.log', level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False

@loader_blueprint.route('/post')
def post_page_post():
    # picture = request.files.get('picture')
    # filename = picture.filename
    # content = request.form.get('content')
    # picture.save(f'./uploads/{filename}')
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_page():
    try:
        picture = request.files.get('picture')
        filename = picture.filename
        if is_filename_allowed(filename):
            content = request.form.get('content')
            picture.save(f'./uploads/images/{filename}')
            new_post(f'./uploads/images/{filename}', content)
            return render_template('post_uploaded.html', content=content, filename=filename)
        else:
            logging.info('Ошибка с расширением файла')
            return 'Ошибка с расширением файла'
    except:
        logging.error('Oшибка загрузки')
        return 'Oшибка загрузки'