from flask import render_template, request, Blueprint
from config import PATH_TO_POSTS_JSON
from functions import load_data, filter_posts


main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates')

search_blueprint = Blueprint('search_blueprint',
                             __name__,
                             template_folder='template')

# вьшка на главную страницу (страница с поиском)
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


# вьшка на страницу с результатами поиска
@search_blueprint.route('/search')
def post_list_page():
    user_search = request.args.get('s')
    posts = load_data(PATH_TO_POSTS_JSON)
    filtered_posts = filter_posts(posts, user_search)

    return render_template("post_list.html", posts=filtered_posts, user_search=user_search)


