# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class StProfile(models.Model):
	"""To keep extra user data"""
	
	#user mapping
	user =models.OneToOneField(User)

	class Meta(object):
		verbose_name = _(u"User Profile")

	#extra user data
	mobile_phone = models.CharField(
		max_length=12,
		blank=False,
		verbose_name=_(u"Mobile Phone"),
		default ='')

	def __unicode__(self):
		return self.user.username