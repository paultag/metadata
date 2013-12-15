from django.shortcuts import render
from metadata.models import Meta

#  /                     => home
#  /metas                => metas
#  /meta/slug            => meta
#  /puzzle/slug          => puzzle
#  /edit/meta/slug       => metaedit
#  /edit/puzzle/slug     => puzzleedit


def home(request):
    return render(request, 'metadata/index.html', {
    }, content_type="text/html")


def metas(request):
    return render(request, 'metadata/metas.html', {
        "metas": Meta.objects.all()
    }, content_type="text/html")
