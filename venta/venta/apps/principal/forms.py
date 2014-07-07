from django.forms import ModelForm
from django import forms
from models import *
class empleadoform(ModelForm):
	class Meta:
		model=empleado
class clienteform(ModelForm):
	class Meta:
		model=cliente

class reservaform(ModelForm):
	class Meta:
		model=reservas
		exclude=["idasiento"]
class paypalform(ModelForm):
	class Meta:
		model=paypal
		exclude=["idres"]
class encuentroform(ModelForm):
	class Meta:
		model=encuentros
class asientoform(ModelForm):
	class Meta:
		model=asientos
