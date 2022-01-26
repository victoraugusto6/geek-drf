import requests
from decouple import config

headers = {'Authorization': config('TOKEN')}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}3/', headers=headers)

assert resultado.status_code == 204
assert len(resultado.text) == 0
