import pytest

from model_mommy import mommy


@pytest.mark.django_db
def test_redirect_to_the_right_url(client):

    mommy.make('shorturls.ShortURL', original='http://www.labcodes.com.br', shortened_slug='test')

    response = client.get('/test/')

    assert response.status_code == 302
    assert response['Location'] == 'http://www.labcodes.com.br'
