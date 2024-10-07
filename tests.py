import requests

class TestCursos:
    headers = {'Authorization': 'Token 85520952b1f4d4edf20ba5eef87f7df0d89e84e2'}
    url_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_cursos, headers=self.headers)

        assert resposta.status_code == 200
    
    def test_post_curso(self):
        teste = {
            "titulo": "Novo Teste",
            "url": "http://www.novoteste.com.br"
        }

        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=teste)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == teste['titulo']

    def test_put_curso(self):
        put = {
            "titulo": "Atualização Teste",
            "url": "http://www.testeatualizacao.com.br"
        }

        resposta = requests.put(url=f'{self.url_cursos}8/', headers=self.headers, data=put)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == put['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_cursos}13/', headers=self.headers)

        assert resposta.status_code == 204

