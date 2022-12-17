from flask import render_template, Blueprint, request
from config import PATH_TO_POSTS_JSON, PATH_TO_LOADED_PICTURES, MESSAGE
from functions import save_post, check_picture


loader_blueprint = Blueprint('loader_blueprint',
                             __name__,
                             template_folder='templates'
                             )


# вьюшка на страницу с формой добавления поста
@loader_blueprint.route('', methods=['GET'])
def post_form_page():
    return render_template('post_form.html')


# вьюшка на страницу с добавленным постом
@loader_blueprint.route('', methods=['POST'])
def post_uploaded_page():
    """получает файл и текст поста от пользователя, сохраняет файл и данные в файл постов"""
    picture = request.files.get('picture')

    message_picture = check_picture(picture)
    if message_picture != MESSAGE['good_picture']:
        return render_template('error_page.html', message=message_picture)

    content = request.form.get('content')
    path_to_pic = f'{PATH_TO_LOADED_PICTURES}{picture.filename}'
    picture.save(path_to_pic)
    new_post = save_post(PATH_TO_POSTS_JSON, path_to_pic, content)

    return render_template('post_uploaded.html', post=new_post)
