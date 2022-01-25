import requests

# GET Avaliações

# avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Status code HTTP
# print(avaliacoes.status_code)

# Acessando dados do Response

# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros

# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados

# print(avaliacoes.json()['next'])

# Acessando resultados desta página

# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados

# print(avaliacoes.json()['results'][0])


# Acessando o último elemento da lista de resultados

# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que realizou a última avaliação

# print(avaliacoes.json()['results'][-1]["nome"])

# GET Avaliação

# avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/4/')

# print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token af58023c8804a7eceaeb8bb88e0290c1517204d4'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
