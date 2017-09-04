import random

import pytest

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from shorturls.models import ShortURL


@pytest.mark.django_db
def test_short_url_str():
    s = ShortURL.objects.create(original='http://labcodes.com.br', shortened_slug='labcodes')
    assert str(s) == 'http://lab.codes/labcodes -> http://labcodes.com.br'


@pytest.mark.django_db
def test_random_generated_slug(mocker):
    with mocker.patch.object(random, 'sample', return_value='random'):
        s = ShortURL.objects.create(original='http://labcodes.com.br')
        assert str(s) == 'http://lab.codes/random -> http://labcodes.com.br'


@pytest.mark.django_db
def test_increment_clicks():
    s = ShortURL.objects.create(original='http://labcodes.com.br', shortened_slug='labcodes')
    assert s.clicks == 0

    s.increment_clicks()
    assert s.clicks == 1


@pytest.mark.django_db
def test_validate_slug():
    with pytest.raises(ValidationError):
        ShortURL.objects.create(original='http://labcodes.com.br', shortened_slug='admin')


@pytest.mark.django_db
def test_validate_duplicate_slug():
    ShortURL.objects.create(original='http://labcodes.com.br', shortened_slug='test')
    with pytest.raises(IntegrityError):
        ShortURL.objects.create(original='http://labcodes.com.br', shortened_slug='test')



@pytest.mark.django_db
def test_unshort_urls(client):
    s = ShortURL.objects.create(original='http://labcodes.com.br', shortened_slug='labcodes')

    response = client.get('/labcodes')
    assert response.status_code == 302
    assert response.url == s.original
