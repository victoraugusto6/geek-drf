from cursos.models import Curso


class TestCursos:

    def test_get_cursos(self, api_client, user):
        api_client.force_authenticate(user)

        response = api_client.get('/api/v2/cursos/')
        assert response.status_code == 200

    def test_get_curso(self, api_client, user, curso):
        api_client.force_authenticate(user)

        response = api_client.get(f'/api/v2/cursos/{curso.pk}/')
        assert response.status_code == 200
        assert response.json()["titulo"] == curso.titulo

    def test_post_curso(self, api_client, user):
        api_client.force_authenticate(user)

        novo = {
            "titulo": "Curso novo cadastrado",
            "url": "https://curso.com/novo-curso"
        }

        response = api_client.post('/api/v2/cursos/', data=novo)
        assert response.status_code == 201
        assert response.json()["titulo"] == novo["titulo"]

    def test_put_curso(self, api_client, user, curso):
        api_client.force_authenticate(user)

        atualizado = {
            "titulo": "Novo Curso de Linux",
            "url": "https://curso.com/linux"
        }

        response = api_client.put(f'/api/v2/cursos/{curso.pk}/', data=atualizado)
        assert response.status_code == 200
        assert response.json()["titulo"] == atualizado["titulo"]
        assert Curso.objects.count() == 1 and Curso.objects.get(titulo='Novo Curso de Linux')

    def test_delete_curso(self, api_client, user, curso):
        api_client.force_authenticate(user)

        response = api_client.delete(f'/api/v2/cursos/{curso.pk}/')
        assert response.status_code == 204
        assert not Curso.objects.exists()
