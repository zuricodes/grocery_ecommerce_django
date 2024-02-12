from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomePageTests(SimpleTestCase):
    """Extends SimpleTestCase"""
    def setUp(self):
        # access homepage
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        #tests if homepage exists
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # check if homepage uses correct template
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_correct_html(self):
        self.assertNotContains(
                self.response, 'Hi! I should not be on the page')
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
                view.func.__name__,
                HomePageView.as_view().__name__)
