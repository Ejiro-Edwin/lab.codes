import pytest

from model_mommy import mommy


@pytest.mark.django_db
def test_increment_clicks():
    s = mommy.make('shorturls.ShortURL')

    assert s.clicks == 0
    s.increment_clicks()

    assert s.clicks == 1
