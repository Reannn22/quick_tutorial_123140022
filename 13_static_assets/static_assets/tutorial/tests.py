import unittest
from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual(response['name'], 'Home View')

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Hi Home View' in res.body)
        
    def test_css(self):
        res = self.testapp.get('/static/app.css', status=200)
        self.assertIn(b'body', res.body)    
