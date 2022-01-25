import requests

headers = {'Authorization': 'Token af58023c8804a7eceaeb8bb88e0290c1517204d4'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

assert resultado.status_code == 200

assert resultado.json()["count"] == 1

assert resultado.json()["results"][0]["titulo"] == 'Linux'
