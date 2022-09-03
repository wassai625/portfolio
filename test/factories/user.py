import factory

from core.models import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'core.User'
        django_get_or_create = ('email',)

        email = 'test3@gmail.com'
