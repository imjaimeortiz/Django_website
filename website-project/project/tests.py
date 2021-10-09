from django.test import TestCase
from .models import Project

# Create your tests here.
class ProjectTests(TestCase):

    def testSetUpData(cls):
        Project.objects.create(title="Example", body="I am writing this to check tests", pub_date="2020-04-31")

    def testSetUp(self):
        project = Project.objects.get(title="This is a sample project")
        field_title = project._meta.get_field('title').verbose_name
        self.assertEquals(field_title, 'title')