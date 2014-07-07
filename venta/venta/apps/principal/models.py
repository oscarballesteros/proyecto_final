from django.db import models

# Create your models here.
class empleado(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	ci=models.IntegerField(unique=True)
	direccion=models.CharField(max_length=200)
	telefono=models.IntegerField(max_length=20)
	email=models.EmailField(max_length=50)
	cargo=models.CharField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "%s "%(self.nombre)




class cliente(models.Model):
	ci=models.CharField(max_length=20)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	telefono=models.IntegerField(max_length=20)
	email=models.EmailField(max_length=75)
	direccion=models.CharField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)
	#asientos=models.ManyToManyField(asientos)
	def __unicode__(self):
		return self.nombre
torneos = (
   ('liga boliviana', 'Liga boliviana'),
   ('libertadores', 'Libertadores'),
   ('sudamericana', 'Sudamericana'),
)
class encuentros(models.Model):
	torneo=models.CharField(max_length=50,choices=torneos)
	equipo1=models.CharField(max_length=50)
	equipo2=models.CharField(max_length=50)
	fecha=models.DateField()
	hora=models.TimeField()	
	curvaN = models.IntegerField()
	curvaS = models.IntegerField()
	general = models.IntegerField()
	preferencia= models.IntegerField()
	def __unicode__(self):
		return "%s vs %s"%(self.equipo1,self.equipo2)

estados = (

   ('disponible', 'Disponible'),
   ('reservado', 'Reservado'),
   ('vendido', 'Vendido'), 
)
sector=(
	('preferencia','Preferencia'),
	('general','General'),
	('curvasur','Curvasur'),
	('curvanorte','Curvanorte'),
)
class asientos(models.Model):
	idencuentros=models.ForeignKey(encuentros)
	estado=models.CharField(max_length=50,choices=estados)
	numero=models.IntegerField()
	sector=models.CharField(max_length=50,choices=sector)
	def __unicode__(self):
		return "%s"%(self.numero)
class reservas(models.Model):
	idasiento=models.ForeignKey(asientos,null=True)
	Nombre=models.CharField(max_length=200,null=True)
	Apellido=models.CharField(max_length=200,null=True)
	CI=models.CharField(max_length=10,null=True)
	telefono=models.IntegerField(max_length=200,null=True)
	fecha=models.DateTimeField(auto_now=True,null=True)
	def __unicode__(self):
		return "%s %s"%(self.Nombre,self.idasiento)

class factura(models.Model):
	idreserva=models.ForeignKey(reservas)
	total=models.FloatField()
	descripcion=models.CharField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)

class galeria(models.Model):
	nombre=models.CharField(max_length=200)
	fotografia=models.ImageField(upload_to='venta/carga')
	def __unicode__(self):
		return "%s "%(self.nombre)

tarjetas = (

   ('visa', 'Visa'),
   ('mastercard', 'Mastercard'),
   ('bnb', 'BnB'),
   ('bancounion', 'BancoUnion'),
   ('bcp', 'BCP'),  
)

class paypal(models.Model):
	idres=models.ForeignKey(reservas,null=True)
	pais=models.CharField(max_length=20,null=True)
	tarjeta=models.CharField(max_length=50,choices=tarjetas,null=True)
	Numero_de_tarjeta=models.CharField(max_length=20,null=True)
	fecha_vencimiento=models.DateField(null=True)
	codigo_seg=models.IntegerField(null=True)
	def __unicode__(self):
		return "%s"%(self.pais)


