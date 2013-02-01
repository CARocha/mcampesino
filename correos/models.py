from django.db import models

# Create your models here.
# 
class Correos(models.Model):
	persona = models.CharField(max_length=150)
	correo = models.EmailField()

	def __unicode__(self):
		return self.persona
	class Meta:
		verbose_name_plural = u'Correos'
