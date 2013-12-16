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

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'metadata.views.home', name='home'),
    url(r'^metas/$', 'metadata.views.metas', name='metas'),
    url(r'^meta/(?P<mid>.*)/$', 'metadata.views.meta', name='meta'),
    url(r'^pick-team/$', 'metadata.views.pick_team', name='pick_team'),
)
