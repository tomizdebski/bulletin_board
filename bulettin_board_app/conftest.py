import pytest
from django.contrib.auth.models import User, Permission

from bulettin_board_app.models import Category, Locations, Announcement, Photos


@pytest.fixture
def user():
    """
    Create fixture user
    :return: queryset user
    """
    return User.objects.create(username='testowy')


@pytest.fixture
def locations():
    """
    Create fixture locations
    :return: queryset loactions
    """
    return Locations.objects.create(city='Warszawa',
                                    street='stuletnia 12',
                                    province='mazowieckie',
                                    zipcode='03-035',
                                    country='Polska',)


@pytest.fixture
def category():
    """
    Create fixture category
    :return:
    """
    return Category.objects.create(name='Test')


@pytest.fixture
def announce(category, locations, user):
    """
    Create fixture announce
    :return: queryset announce
    """
    return Announcement.objects.create(
        name='Test',
        description='Test-desc',
        category_id=category.id,
        locations_id=locations.id,
        user_id=user.id
        )


@pytest.fixture
def photo(announce):
    """
    Create fixture photo
    :param announce:
    :return:
    """
    return Photos.objects.create(
        name='Test',
        img='images/test.jpg',
        announcement_id=announce.id
    )



