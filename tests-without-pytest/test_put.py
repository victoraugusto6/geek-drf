import requests
from decouple import config

headers = {'Authorization': config('TOKEN')}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Curso de Windows Atualizado",
    "url": "https://curso.com/windows"
}

# curso = requests.get(url=f'{url_base_cursos}2/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}2/', headers=headers, data=curso_atualizado)

assert resultado.status_code == 200

assert resultado.json()["titulo"] == curso_atualizado["titulo"]
