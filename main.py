import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, "overwrite": "False"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, path_to_file: str, filename: str):
        href = self._get_upload_link(path_to_file=path_to_file).get('href', "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Upload success')



if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к загружаемому файлу: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload_file(path_to_file, filename)