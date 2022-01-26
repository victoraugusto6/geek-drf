import requests
from decouple import config

headers = {'Authorization': config('TOKEN')}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Aprendendo Mac",
    "url": "https://curso.com/mac"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == 201
assert resultado.json()["titulo"] == novo_curso["titulo"]
