import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, path_to_ya: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_ya, "overwrite": "False"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, path_to_file: str):
        # path_conv = path_to_file.split('\\', 1)
        # path_to_ya = (path_conv[1]).replace('\\', '/')
        path_conv = path_to_file.split('\\')
        path_to_ya = (path_conv[-1]).replace('\\', '/')
        href = self._get_upload_link(path_to_ya=path_to_ya).get('href', "")
        # print(href)
        # filename = path_to_file.split("\\").sort()
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Upload success')



if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к загружаемому файлу (например: A:\\file.txt): ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload_file(path_to_file)

# path_to_file = input('Введите путь к загружаемому файлу (например: A:\\file.txt): ')
# path_conv = path_to_file.split('\\', 1)
# path_to_ya = (path_conv[1]).replace('\\', '/')
# print(path_to_ya)