import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework.test import APIClient

from cursos.models import Curso


# API
@pytest.fixture
def api_client():
    return APIClient()


# User
@pytest.fixture
def user(db):
    return User.objects.create_superuser(
        username='test_user',
        password='test_pass'
    )


@pytest.fixture
def curso(db):
    return baker.make(Curso)
