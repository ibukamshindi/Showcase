from django.test import TestCase
from .models import Image,Projects,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(profile_photo='this is me',bio='execeptional')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)  

class ImageTestClass(TestCase):
  
    def setUp(self):
        self.image = Image(image ='imageurl', description='My first project')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

class ProjectsTestCase(TestCase):
    def setUp(self):
        self.projects=Projects(project_name='landingpage', project_photo='screenshot', description='some description', github_repo='git repo', url='how.com', owner='kk')

    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Projects))                