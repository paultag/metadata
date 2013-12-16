from django.shortcuts import render, redirect
from metadata.models import Meta, PuzzleTeamMembership, PuzzleTeam

#  /                     => home
#  /metas                => metas
#  /meta/slug            => meta
#  /puzzle/slug          => puzzle
#  /edit/meta/slug       => metaedit
#  /edit/puzzle/slug     => puzzleedit


def home(request):
    return render(request, 'metadata/index.html', {
    }, content_type="text/html")


def pick_team(request):
    user = request.user
    try:
        membership = PuzzleTeamMembership.objects.get(member=user.id)
    except PuzzleTeamMembership.DoesNotExist:
        membership = None

    if request.method == 'POST':
        team = PuzzleTeam.objects.get(id=request.POST['team'])

        if membership is None:
            membership = PuzzleTeamMembership(member=user, team=team)
        else:
            membership.team = team
        membership.save()
        return redirect(metas)

    else:
        return render(request, 'metadata/pick-team.html', {
            "teams": PuzzleTeam.objects.all(),
            "membership": membership,
        }, content_type="text/html")


def metas(request):
    user = request.user
    try:
        team = PuzzleTeamMembership.objects.get(member=user.id)
    except PuzzleTeamMembership.DoesNotExist:
        return redirect(pick_team)

    return render(request, 'metadata/metas.html', {
        "user": user,
        "team": team,
        "metas": metas,
    }, content_type="text/html")
