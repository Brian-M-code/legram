from django.test import TestCase
from .models import Image
from django.urls import reverse

# Create your tests here.
class ImagetModelTest(TestCase):
    
    def setUp(self):
        Image.objects.create(image='x6.jpg')
    
    def test_image_content(self):
        image=Image.objects.get(id=1)
        expected_object_name = f'{image.image}'
        self.assertEqual(expected_object_name, 'x6.jpg')
        
class HomePageViewTest(TestCase):
    def setUp(self):
        Image.objects.create(image='x6.jpg')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'home.html')