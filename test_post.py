import requests

headers = {'Authorization': 'Token af58023c8804a7eceaeb8bb88e0290c1517204d4'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Aprendendo Mac",
    "url": "https://curso.com/mac"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == 201
assert resultado.json()["titulo"] == novo_curso["titulo"]
