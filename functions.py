import json


def load_json():
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_content(form):
    return [i for i in load_json() if form.lower() in i['content'].lower()]


def new_post(pic, content):
    list_ = load_json()
    list_.append({'pic': pic, 'content': content})
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(list_, file)