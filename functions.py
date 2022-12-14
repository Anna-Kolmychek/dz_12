import json
import logging
import os
from config import MESSAGE, ALLOWED_EXTENSIONS


# Задаем настройки логгера

logging.basicConfig(filename=os.path.join('logs', 'api.log'),
                    format='"%(levelname)s : %(message)s"',
                    level=logging.INFO,
                    encoding='utf-8'
                    )


def load_data(path_to_file: str) -> list[dict]:
    """загружает json-данные из файла"""
    try:
        with open(path_to_file, 'r', encoding='utf-8') as data_file:
            loaded_data = json.load(data_file)
    except FileNotFoundError:
        logging.error(MESSAGE['file_not_exist'])
        loaded_data = []
    except json.JSONDecodeError:
        logging.error(MESSAGE['bаd_json'])
        loaded_data = []

    return loaded_data


def save_data(path_to_file: str, posts: list[dict]):
    """записывает json-данные в файл"""
    with open(path_to_file, 'w', encoding='utf-8') as data_file:
        data_file.write(json.dumps(posts, ensure_ascii=False, indent=2))


def filter_posts(posts: list[dict], search_str: str) -> list[dict]:
    """возвращает только посты содержащие подстроку"""
    filtered_posts = []

    for post in posts:
        if search_str.lower() in post['content'].lower():
            filtered_posts.append(post)

    return filtered_posts


def save_post(path_to_posts_json, path_to_pic, content):
    """сохраняет новый пост в файл, возвращает пост в формате словаря"""
    new_post = {"pic": path_to_pic,
                "content": content}

    posts = load_data(path_to_posts_json)
    posts.append(new_post)
    save_data(path_to_posts_json, posts)

    return new_post


def check_picture(picture):
    """проверяет, является ли загруженный файл картинкой"""
    if not picture:
        logging.info(MESSAGE['not_uploaded'])
        return MESSAGE['not_uploaded']

    if picture.filename.split('.')[-1].lower() not in ALLOWED_EXTENSIONS:
        logging.info(MESSAGE['not_img'])
        return MESSAGE['not_img']

    return MESSAGE['good_picture']
