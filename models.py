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

__date__ = "2014-05-20"
__author__ = "vittoros"

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from ecm.plugins.assets.models import Asset
from ecm.apps.eve.models import Type, CelestialObject
from ecm.apps.corp.models import Hangar, Corporation
from sha import sha
from random import random

#------------------------------------------------------------------------------
class Report(models.Model):
    name = models.CharField(max_length=255)
    systemID = models.BigIntegerField(null=True, blank=True)
    stationID = models.BigIntegerField(null=True, blank=True)
    hangarID = models.PositiveIntegerField(null=True, blank=True) # hangar division
    key = models.CharField(max_length=255, editable=False)

    def __unicode__(self):
        return self.name

    def generate_key(self):
        checksum = sha()
        checksum.update('%s%s' % (random(), self.name))
        self.key = checksum.hexdigest()

    def system(self):
        try:
            return CelestialObject.objects.get(itemID=self.systemID).itemName
        except CelestialObject.DoesNotExist:
            return self.systemID

    def station(self):
        try:
            return CelestialObject.objects.get(itemID=self.stationID).itemName
        except CelestialObject.DoesNotExist:
            return self.stationID

    def hangar(self):
        try:
            return Hangar.objects.get(hangarID=self.hangarID) \
                    .get_name(Corporation.objects.mine())
        except Hangar.DoesNotExist:
            return self.hangarID

    def filter_assets(self):
        assets = Asset.objects.all()
        if self.systemID:
            assets = assets.filter(solarSystemID=self.systemID)
        if self.stationID:
            assets = assets.filter(stationID=self.stationID)
        if self.hangarID:
            assets = assets.filter(hangarID=self.hangarID)
        return assets

    def generate_csv(self):
        assets = self.filter_assets()
        aggregate = assets.values('eve_type__typeID', 'eve_type__typeName') \
                .order_by('eve_type__typeName') \
                .annotate(total=Sum('quantity'))

        return "\n".join(map(lambda item: ';'.join((
            unicode(item['eve_type__typeID']),
            item['eve_type__typeName'],
            unicode(item['total']))), aggregate))
