# portfolio/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Project
from .forms import ContactForm  # Asegúrate de que tienes ContactForm

#Test for contact form
class ContactFormTest(TestCase):
    
    def test_sql_injection_in_contact_form(self):
        #Creates a malicious input that attempts to inject SQL
        form_data = {
            'name': "Gonzalo", 
            'message': "' OR 1=1 --"  # Malicious input
        }
        form = ContactForm(data=form_data)
        
        # Check that the form is not valid
        self.assertFalse(form.is_valid(), "The form accepted malicious SQL input")

#Tests for the models
class ProjectModelTest(TestCase):
    
    def setUp(self):
        # Crear una instancia de Project para pruebas
        self.project = Project.objects.create(
            title="Test Project",
            description="This is a test project.",
            technologies="Django, Python",
            link="https://github.com/Gonzalo5351/test-project",
            date="2024-10-13"
        )

    def test_project_creation(self):
        # Verificar que el proyecto se ha creado correctamente
        project = Project.objects.get(id=self.project.id)
        self.assertEqual(project.title, "Test Project")
        self.assertEqual(project.description, "This is a test project.")

# Pruebas para las vistas
class ProjectViewsTest(TestCase):

    def setUp(self):
        # Crear un proyecto para usar en la prueba de la vista
        Project.objects.create(
            title="Test Project",
            description="This is a test project.",
            technologies="Django, Python",
            link="https://github.com/Gonzalo5351/test-project",
            date="2024-10-13"
        )

    def test_project_list_view(self):
        # Verificar que la vista de lista de proyectos devuelve un código 200
        response = self.client.get(reverse('project_list'), follow=True) # Follow the redirect
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")
