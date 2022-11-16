from django.db import models


class Nivel(models.Model):

    JUNIOR = 'junior'
    SEMIJUNIOR = 'semijunior'
    SENIOR = 'senior'

    CATEGORIES_CHOICES = (
        (JUNIOR, 'Junior'),
        (SEMIJUNIOR, 'Semijunior'),
        (SENIOR, 'Senior'),
    )

    FRONTEND = 'frontend'
    BACKEND = 'backend'

    PERFIL_CHOICES = (
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
     
    )

    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    release_date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    category_perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES)