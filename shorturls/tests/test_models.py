import random

import pytest

from model_mommy import mommy

from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_increment_clicks():
    s = mommy.make('shorturls.ShortURL')

    assert s.clicks == 0
    s.increment_clicks()

    assert s.clicks == 1


@pytest.mark.django_db
def test_clean_shorturl():
    with pytest.raises(ValidationError):
        mommy.make('shorturls.ShortURL', shortened_slug='admin')


@pytest.mark.django_db
def test_short_url_str_repr():
    s = mommy.make('shorturls.ShortURL', shortened_slug='slug', original='test.com')

    assert str(s) == 'http://lab.codes/slug -> test.com'


@pytest.mark.django_db
def test_shorturl_generates_slug(mocker):
    with mocker.patch.object(random, 'sample', return_value='random'):
        s = mommy.make('shorturls.ShortURL', original='test.com')

        assert s.shortened_slug == 'random'
