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


LINK_TYPES = (
    ('pdf', 'PDF'),
    ('doc', 'Document'),
    ('img', 'Image'),
)


class Meta(models.Model):
    author = models.ForeignKey(User)
    answer = models.CharField(max_length='128')


class MetaDocument(models.Model):
    author = models.ForeignKey(User)
    link = models.URLField()
    link_type = models.CharField(max_length=64, choices=LINK_TYPES)


class Puzzle(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length='128')


class PuzzleDocument(models.Model):
    author = models.ForeignKey(User)
    link = models.URLField()
    link_type = models.CharField(max_length=64, choices=LINK_TYPES)
