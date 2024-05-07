from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user_a_username = "sina"
        self.user_a_pw = "pass"

        user_a = User.objects.create(
            username=self.user_a_username, email="s.e.sezza121@gmail.com"
        )

        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(self.user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        user_qs = User.objects.filter(username__iexact="sina")
        user_exists = user_qs.exists() and user_qs.count() == 1
        self.assertTrue(user_exists)
        sina = user_qs.first()
        self.assertTrue(sina.check_password(self.user_a_pw))

    def test_login_url(self):
        # login_url = '/login/'
        # self.assertEqual(settings.LOGIN_URL, login_url)

        login_url = settings.LOGIN_URL

        data = {"username": self.user_a_username, "password": self.user_a_pw}
        response = self.client.post(path=login_url, data=data, follow=True)

        # print(dir(response))
        # print(f"response status code is {response.status_code}")

        redirect_path = response.request.get("PATH_INFO")
        # print(f"redirect path is {redirect_path}")
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)

        self.assertEqual(response.status_code, 200)

    def test_login(self):
        logged_in = self.client.login(
            username=self.user_a_username, password=self.user_a_pw
        )

        print(logged_in)
        self.assertTrue(logged_in)

        # uid = c.session['_auth_user_hash']
        # user = User._meta.model.objects.get(pk=uid)
        # self.assertEqual(user.username, self.user_a_username)
