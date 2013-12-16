# Copyright (c) 2013, Paul R. Tagliamonte <tag@pault.ag>
# 
# This file is part of metadata.
# 
# metadata is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User


def generic_str(what):
    def _(self):
        return "<%s:%s>" % (self.__class__.__name__, getattr(self, what))
    return _


LINK_TYPES = (
    ('pdf', 'PDF'),
    ('doc', 'Document'),
    ('img', 'Image'),
)


class PuzzleTeam(models.Model):
    name = models.CharField(max_length='128')
    __str__ = generic_str('name')


class Meta(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length='128')
    answer = models.CharField(max_length='128')
    team = models.ForeignKey(PuzzleTeam, related_name='metas')

    # <p>({{meta.puzzles_solved}} / {{meta.puzzles_total}} solved)</p>

    def puzzles_solved(self):
        return self.puzzles.filter(solved=True).count()

    def puzzles_total(self):
        return self.puzzles.count()

    __str__ = generic_str('title')


class MetaDocument(models.Model):
    author = models.ForeignKey(User)
    link = models.URLField()
    link_type = models.CharField(max_length=64, choices=LINK_TYPES)


class Puzzle(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length='128')
    meta = models.ForeignKey(Meta, related_name='puzzles')
    solved = models.BooleanField()
    answer = models.CharField(max_length='128')

    __str__ = generic_str('title')


class PuzzleDocument(models.Model):
    author = models.ForeignKey(User)
    link = models.URLField()
    link_type = models.CharField(max_length=64, choices=LINK_TYPES)


class PuzzleTeamMembership(models.Model):
    member = models.ForeignKey(User)
    team = models.ForeignKey(PuzzleTeam)

    def __str__(self):
        return "<%s, on the %s team>" % (self.author.username,
                                               self.team.name)
