import user

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models    import User
from django.test import TestCase
from models    import UserProfile, Game, Achievement,Clan
from steam_app import models
from steam_app.forms import GameForm


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'test1',
            'password': '1'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.login(**self.credentials)
        self.assertTrue(response)

class test_register1(TestCase):

    def test_register(self):

        user1 = User.objects.create(username="pepe")
        user = UserProfile.objects.create(user=user1)
        self.assertEqual(user1, user.user)

class test_2(TestCase):
    def test_n(self):
        user1 = User.objects.create(username="user")
        juego = Game.objects.create(user=user1,appid="1789", name="Fifa")
        test_np = Achievement.objects.create(user=user1,name='Correr',appid_game=juego)

        self.assertEqual(juego.id, test_np.appid_game.id)
class CreateGameTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'test2',
            'password': '2'}
        u = User.objects.create_user(**self.credentials)
        self.Game = {
            'appid': '4444',
            'name': '2K17',
            'version': '2',
            'company': 'EA',
            'opinion': 'Good',
        }
        self.ccount = Game.objects.count()
        self.client.login(**self.credentials)

    def test_createGame(self):
        form = GameForm(data=self.Game)
        self.assertTrue(form.is_valid())
        response = self.client.post('/game/', self.Game)
        self.assertEqual(response.status_code, 302)
        self.client.logout()

class EditGameTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'test3',
            'password': '3'}
        u = User.objects.create_user(**self.credentials)
        self.Game = {
            'appid': '4444',
            'name': '2K17',
            'version': '2',
            'company': 'EA',
            'opinion': 'Good',
        }
        self.ModGame = {
            'appid': '4444',
            'name': '2K17',
            'version': '3',
            'company': 'EASPORTS',
            'opinion': 'Good, not at all',
        }
        self.client.login(**self.credentials)
        self.client.post('/game/', self.Game)


    def test_editGame(self):
        response = self.client.post('/change/game/' + '1/' , self.ModGame)

        self.assertEqual(response.status_code, 302)
        self.client.logout()