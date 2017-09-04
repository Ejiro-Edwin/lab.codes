from django.shortcuts import redirect

from shorturls.models import ShortURL


def unshort_url(request, slug):
    s = ShortURL.objects.get(shortened_slug=slug)
    s.increment_clicks()
    return redirect(s.original)
