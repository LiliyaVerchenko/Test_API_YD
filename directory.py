import requests
from pprint import pprint
token = 'OAuth AgAAAAAQNAdaAADLW27VORimwUUkvF8jB7ys7Js'
headers_YD = {'Accept': 'application/json', 'Authorization': token}
name_directory = 'Photo'

def create_directory():
    #получаем список папок на диске
    response_list = requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F',
                                 headers=headers_YD)
    dir_info = response_list.json()['_embedded']['items']
    list_dir = [dir['name'] for dir in dir_info]
    if name_directory in list_dir:
        print(f'Папка с именем "{name_directory}" уже существует')
        return name_directory
    response = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path={name_directory}',
                            headers=headers_YD)
    print(f'Папка c именем "{name_directory}" успешно добавлена в каталог')
    return name_directory

# create_directory()