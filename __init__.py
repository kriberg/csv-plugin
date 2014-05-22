# Copyright (c) 2010-2013 Kristian Berg
#
# This file is part of csv-plugin.
#
# csv-plugin is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# csv-plugin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# csv-plugin. If not, see <http://www.gnu.org/licenses/>.

__date__ = "2014-05-20"
__author__ = "vittoros"

from django.utils.translation import ugettext_lazy as tr_lazy

NAME = 'csv'
VERSION = '1.0'

DEPENDS_ON = {
    'ecm' : '2.0',
    'ecm.plugins.assets' : '2.0',
}

MENUS = [
    {'title': tr_lazy('CSV'),    'url': '',      'items': [
    ]},
]

URL_PERMISSIONS = [
    r'^/csv/.*$',
]

SETTINGS = {
}


