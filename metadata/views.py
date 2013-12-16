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
        membership = PuzzleTeamMembership.objects.get(member=user.id)
    except PuzzleTeamMembership.DoesNotExist:
        return redirect(pick_team)

    team = membership.team
    metas = team.metas

    return render(request, 'metadata/metas.html', {
        "user": user,
        "team": team,
        "metas": metas,
    }, content_type="text/html")


def meta(request, mid):
    user = request.user
    try:
        membership = PuzzleTeamMembership.objects.get(member=user.id)
    except PuzzleTeamMembership.DoesNotExist:
        return redirect(pick_team)
    team = membership.team

    try:
        meta = Meta.objects.get(id=mid)
    except Meta.DoesNotExist:
        return redirect(home)

    if meta.team != team:
        return redirect(home)

    return render(request, 'metadata/meta.html', {
        "meta": meta,
        "team": team,
        "membership": membership,
        "user": user,
    }, content_type="text/html")
