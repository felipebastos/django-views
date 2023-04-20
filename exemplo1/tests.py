from django.test import TestCase, Client

# Create your tests here.
class Exemplo1TestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_disse_oi(self):
        resp = self.client.get('/exemplo1/digaOi/')

        self.assertEqual(200, resp.status_code)
        self.assertEqual(b'Oi!', resp.content)

    def test_disse_oi_e_nome(self):
        nome = 'Reperquilson'

        resp = self.client.get(f'/exemplo1/digaOi/{nome}/')

        self.assertEqual(200, resp.status_code)
        self.assertEqual(b'Oi Reperquilson!', resp.content)
