from django.shortcuts import render

#  /                     => home
#  /metas                => metas
#  /meta/slug            => meta
#  /puzzle/slug          => puzzle
#  /edit                 => edit
#  /edit/meta/slug       => edit meta
#  /edit/puzzle/slug     => edit puzzle


def home(request):
    return render(request, 'metadata/index.html', {},
                  content_type="text/html")
