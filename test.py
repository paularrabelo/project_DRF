import requests
import unittest


class TestCursos(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.headers = {'Authorization': 'Token 85520952b1f4d4edf20ba5eef87f7df0d89e84e2'}
        cls.url_cursos = 'http://localhost:8000/api/v2/cursos/'

    
    def test_get_cursos(self):
        response = requests.get(url=self.url_cursos, headers=self.headers)

        self.assertEqual(response.status_code, 200)
    
    
    def test_post_curso(self):
        teste = {
            "titulo": "Teste novo 3",
            "url": "http://www.testenovo3.com.br"
        }

        response = requests.post(url=self.url_cursos, headers=self.headers, json=teste)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['titulo'], teste['titulo'])

    
    def test_put_curso(self):
        put = {
            "titulo": "Nova Atualização",
            "url": "http://www.atualizacaoteste.com.br"
        }

        response = requests.put(url=f'{self.url_cursos}8/', headers=self.headers, json=put)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['titulo'], put['titulo'])

    
    def test_delete_curso(self):
        response = requests.delete(url=f'{self.url_cursos}9/', headers=self.headers)

        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()