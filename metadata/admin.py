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

from django.contrib import admin
from metadata.models import (Meta, MetaDocument, Puzzle, PuzzleDocument,
                             PuzzleTeam, PuzzleTeamMembership)


class MetaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Meta, MetaAdmin)


class MetaDocumentAdmin(admin.ModelAdmin):
    pass
admin.site.register(MetaDocument, MetaDocumentAdmin)


class PuzzleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Puzzle, PuzzleAdmin)


class PuzzleDocumentAdmin(admin.ModelAdmin):
    pass
admin.site.register(PuzzleDocument, PuzzleDocumentAdmin)


class PuzzleTeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(PuzzleTeam, PuzzleTeamAdmin)


class PuzzleTeamMembershipAdmin(admin.ModelAdmin):
    pass
admin.site.register(PuzzleTeamMembership, PuzzleTeamMembershipAdmin)
