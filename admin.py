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

from django.contrib import admin
from django.db.models import Q
from django import forms

from ecm.apps.eve.models import CelestialObject
from ecm.apps.corp.models import CorpHangar
from ext_plugins.csv.models import Report

class ReportForm(forms.ModelForm):
    systemID = forms.ModelChoiceField(queryset=CelestialObject.objects \
            .filter(group=5).order_by('itemName'), required=False)
    stationID = forms.ModelChoiceField(queryset=CelestialObject.objects \
            .filter(Q(group=15) | Q(type=21645)).order_by('itemName'),
            required=False)
    hangarID = forms.ModelChoiceField(queryset=CorpHangar.objects.all(),
            required=False)

    def clean_systemID(self):
        system = self.cleaned_data.get('systemID', None)
        if system:
            return system.itemID

    def clean_stationID(self):
        station = self.cleaned_data.get('stationID', None)
        if station:
            return station.itemID

    def clean_hangarID(self):
        hangar = self.cleaned_data.get('hangarID', None)
        if hangar:
            return hangar.hangar_id

    class Meta:
        model = Report


class ReportAdmin(admin.ModelAdmin):
    form = ReportForm
    readonly_fields = ('key',)

    def save_model(self, request, obj, form, change):
        if not obj.key:
            obj.generate_key()
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        obj.save()


admin.site.register(Report, ReportAdmin)
