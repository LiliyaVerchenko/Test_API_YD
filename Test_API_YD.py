import unittest
import requests
from directory import create_directory, headers_YD, token
from pprint import pprint

class TestDocs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_create_directory1(self):      # статус создания папки "Photo" - 201 (успешно)
        response = requests.put(f'https://cloud-api.yandex.net:443/v1/disk/resources?path=%2FPhoto10',
                                headers=headers_YD)
        self.assertEqual(response.status_code, 201)

    def test_create_directory2(self):   # статуc 409 - папка "Photo_VK" уже существует
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources?path=%2FPhoto_VK',
                                headers=headers_YD)
        self.assertEqual(response.status_code, 409)

    def test_create_directory3(self): # негативный тест, статус создания новой папки "Photo_32"!= 409
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources?path=%2FPhoto_32',
                                headers=headers_YD)
        self.assertFalse(response.status_code == 409)

    def test_create_directory4(self):      # проверка на наличие папки "Photo_VK" в общем списке файлов
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F',
                                    headers=headers_YD)
        dir_info = response.json()['_embedded']['items']
        list_dir = [dir['name'] for dir in dir_info]   # получили список файлов
        self.assertIn('Photo_VK', list_dir)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

if __name__ == '__main__':
    unittest.main()

