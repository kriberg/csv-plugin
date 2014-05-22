# Copyright (c) 2010-2014 Kristian Berg
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

__date__ = "2014-05-22"
__author__ = "vittoros"

from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext as Ctx
from django.http import HttpResponse

from ecm.views.decorators import check_user_access
from ext_plugins.csv.models import Report

#------------------------------------------------------------------------------
@check_user_access()
def home(request):
    reports = Report.objects.all()
    return render_to_response('ecm/csv/reports.html', {
        'reports': reports,
        }, Ctx(request))

@check_user_access()
def csv_report(request, key):
    report = get_object_or_404(Report, key=key)
    return HttpResponse(report.generate_csv())
