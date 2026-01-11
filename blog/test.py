from django.test import TestCase
from django.urls import reverse


class UrlsTests(TestCase):
    def test_urls(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('new_post'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('detail_post', args=[9]))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('edit_post', args=[9]))
        self.assertEqual(response.status_code, 200)

    def test_views(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

        response = self.client.get(reverse('new_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'PostForm.html')

        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_posts.html')

        response = self.client.get(reverse('detail_post', args=[9]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_post.html')