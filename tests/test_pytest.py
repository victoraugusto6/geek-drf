import requests
from decouple import config


class TestCursos:
    headers = {'Authorization': config('TOKEN')}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)
        assert curso.status_code == 200
        assert curso.json()["titulo"] == 'Linux'

    def test_post_curso(self):
        novo = {
            "titulo": "Curso novo cadastrado",
            "url": "https://curso.com/novo-curso"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()["titulo"] == novo["titulo"]

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Linux",
            "url": "https://curso.com/linux"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}1/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Linux 2",
            "url": "https://curso.com/linux-2"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}1/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
        assert resposta.json()["titulo"] == atualizado["titulo"]

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}1/', headers=self.headers)
        assert resposta.status_code == 204
        assert resposta.text == 0
