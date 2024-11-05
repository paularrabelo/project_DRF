from django.test import LiveServerTestCase
import requests

class TestCursos(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.headers = {'Authorization': 'Token 8a2f1eade9407db7d59efc72e4821564ece69825'}
        cls.url_cursos = f'{cls.live_server_url}/api/v2/cursos/'

    def test_get_cursos(self): 
        response = requests.get(url=self.url_cursos, headers=self.headers)
        self.assertEqual(response.status_code, 200, msg=f"Erro: {response.text}")

    def test_post_curso(self):
        teste = {
            "titulo": "Novo curso de teste",
            "url": "http://www.novocursodeteste.com.br"
        }
        response = requests.post(url=self.url_cursos, headers=self.headers, json=teste)
        self.assertEqual(response.status_code, 201, msg=f"Erro: {response.text}")

    def test_put_curso(self):
        put = {
            "titulo": "Atualização nova de teste",
            "url": "http://www.atualizacaonovadeteste.com.br"
        }
        response = requests.put(url=f'{self.url_cursos}1/', headers=self.headers, json=put)
        self.assertEqual(response.status_code, 200, msg=f"Erro: {response.text}")

    def test_delete_curso(self): 
        response = requests.delete(url=f'{self.url_cursos}14/', headers=self.headers)
        self.assertEqual(response.status_code, 204, msg=f"Erro: {response.text}")
