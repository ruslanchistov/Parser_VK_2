""" Собираем текстовую информацию со стены ВК """
import os
import requests
import json
from vk_data import Data


def get_wall_posts(group_name, count_post, data):
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count={count_post}&access_token={data}&v=5.52"
    req = requests.get(url)
    src = req.json()
    # print(src) # Промежуточная проверка ([200]).

    """Проверяем существует ли директория с именем группы"""
    if os.path.exists(f"{group_name}"):
        print(f"Директория группы с именем {group_name} уже существует")
    else:
        os.mkdir(group_name)  # Создаём директорию в нашем проекте.

    """ Сохраняем в JSON файл """
    with open(f"{group_name}/{group_name}", 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    try:
        # with open(f"{group_name}/{group_name}",'r',encoding='utf-8') as file:
        #     src = json.load(file)
        #     Используем данные из файла,
        #     чтобы не заходить каждый раз на сайт при отладке.

        """ Вытаскиваем данные из постов и записываем их в текстовый файл """
        with open(f"{group_name}/{group_name}_text.txt", 'w', encoding='utf-8') as file:
            for post in src['response']['items']:
                file.write(post.get("text", ' ') + '\n')
    except IOError:
        print("Что-то пошло не так !!!")


def main():
    group_name = input('Введите имя группы: ')
    count_post = input('Введите количество постов для парсинга: ')
    data = Data.getter()
    get_wall_posts(group_name, count_post, data)


if __name__ == '__main__':
    main()
