from django.shortcuts import render, render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from forms import *
from models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from venta.settings import RUTA_PROYECTO
import pdb
from django.core.urlresolvers import reverse
import os
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from datetime import date,time,datetime
#import datetime
# Create your views here.
def inicio(request):
	
	return render_to_response('index.html',{},RequestContext(request))
def inicio1(request):
	
	return render_to_response('index1.html',{},RequestContext(request))


def inicio2(request):
	
	return render_to_response('index2.html',{},RequestContext(request))

def inicio3(request):
	
	return render_to_response('index3.html',{},RequestContext(request))
def reservass(request):
	
	return render_to_response('reservass.html',{},RequestContext(request))
def nuevousuario(request):
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/index')
	else:
		formulario=UserCreationForm()
	return render_to_response('regisusuario.html',{'formulario':formulario},context_instance=RequestContext(request))
def ingresar(request):
	if request.method=='POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/index2')
				else:
					return render_to_response('noactivo.html',context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')

def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

#pagina de registro de habitacion
@login_required(login_url='/ingresar')

def index(request):
	return render_to_response('index.html',{},RequestContext(request))
#@login_required(login_url='/ingresar')

def regiscliente(request):
	if request.method=='POST':
		formu=clienteform(request.POST)
		if formu.is_valid():
			formu.save()
			return HttpResponseRedirect('/clientes')
	else:
		formu=clienteform()

	#return render_to_response('clientereg.html',{},context_instance=RequestContext(request))
	return render_to_response('regiscliente.html',{'formu':formu},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def clientes(request):
	client=cliente.objects.all()
	return render_to_response('clientereg.html',{},context_instance=RequestContext(request))
	#return render_to_response('client.html',{'client':client},context_instance=RequestContext(request))

def clientesregis(request):
	datos=cliente.objects.all()
	return render_to_response('client.html',{'datos':datos},context_instance=RequestContext(request))

def desigpartido(request):
	
	if request.method=='POST':
		formulario=encuentroform(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/index2')
	else:
		formulario=encuentroform()

	return render_to_response('encuentros.html',{'formu':formulario},RequestContext(request))
def designarasiento(request):
	if request.method=='POST':
		formulario=asientoform(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/index2')
	else:
		formulario=asientoform()
	return render_to_response('desigasientos.html',{'formu':formulario},RequestContext(request))



#def hola(request):
#	return render_to_response("index.html",{"fecha":datetime.datetime.today()})


def sectors(request,id):
	enc=get_object_or_404(encuentros,pk=id)
	return render_to_response('sectores.html',{'enc':enc},RequestContext(request))

def preferencias(request,id):
	#pdb.set_trace()
	enc=get_object_or_404(encuentros,pk=id)
	i=1
	#pdb.set_trace()
	a=asientos.objects.filter(sector='preferencia',idencuentros=id).count()
	if a==0:
		while i <= 1037:
			asi = asientos()
			asi.idencuentros= enc
			asi.estado= 'disponible'
			asi.numero= i
			asi.sector='preferencia'
			asi.save()
			i+=1


	res=asientos.objects.filter(sector='preferencia',idencuentros=id)
	return render_to_response('preferencia.html',{'res':res,'enc':enc},RequestContext(request))
def generals(request,id):
	enc=get_object_or_404(encuentros,pk=id)
	i=2075
	#pdb.set_trace()
	a=asientos.objects.filter(sector='general',idencuentros=id).count()
	if a==0:
		while i <= 3111:
			asi = asientos()
			asi.idencuentros= enc
			asi.estado= 'disponible'
			asi.numero= i
			asi.sector='general'
			asi.save()
			i+=1


	res=asientos.objects.filter(sector='general',idencuentros=id)
	return render_to_response('gral.html',{'res':res,'enc':enc},RequestContext(request))

def curvasur(request,id):
	enc=get_object_or_404(encuentros,pk=id)
	i=1038
	a=asientos.objects.filter(sector='curvasur',idencuentros=id).count()
	if a==0:
		while i <= 2074:
			asi = asientos()
			asi.idencuentros= enc
			asi.estado= 'disponible'
			asi.numero= i
			asi.sector='curvasur'
			asi.save()
			i+=1
	res=asientos.objects.filter(sector='curvasur',idencuentros=id)
	return render_to_response('csur.html',{'res':res,'enc':enc},RequestContext(request))


def curvanorte(request,id):
	#pdb.set_trace()
	enc=get_object_or_404(encuentros,pk=id)
	i=3112
	#pdb.set_trace()
	a=asientos.objects.filter(sector='curvanorte',idencuentros=id).count()
	if a==0:
		while i <= 4148:
			asi = asientos()
			asi.idencuentros= enc
			asi.estado= 'disponible'
			asi.numero= i
			asi.sector='curvanorte'
			asi.save()
			i+=1


	res=asientos.objects.filter(sector='curvanorte',idencuentros=id)
	return render_to_response('cnorte.html',{'res':res,'enc':enc},RequestContext(request))

def reservacion(request,id):
	#pdb.set_trace()
	asi=get_object_or_404(asientos,pk=id) 
	#res=get_object_or_404(paypal,)
	if request.method=='POST':
		formulario=reservaform(request.POST)
		#reservas.objects.filter(pk=int(j))
		if formulario.is_valid():
			form=formulario.save()
			form.idasiento=asi
			form.save()
			asi.estado="reservado"
			asi.save()

			return HttpResponseRedirect(reverse(paypal,args=[id]))
	else:
		data={
			"asiento":asi.numero,
		}
		formulario=reservaform(data)

	return render_to_response('reserva.html',{'formu':formulario,'asi':asi},RequestContext(request))

def partidos(request):
	par=encuentros.objects.all()
	return render_to_response('partidos.html',{'par':par},RequestContext(request))

def paypal(request,id):
	res=get_object_or_404(reservas,idasiento=id)
	#pdb.set_trace()
	asi=get_object_or_404(asientos,pk=id)
	if request.method=='POST':
		formulario=paypalform(request.POST)
		if formulario.is_valid():
			#pdb.set_trace()
			form=formulario.save()
			form.idres=res
			form.save()
			#pdb.set_trace()
			asi.estado="vendido"
			asi.save()

			return HttpResponseRedirect(reverse(crear_reporte,args=[asi.id]))
		
	else:
		formulario=paypalform()

	return render_to_response('pago.html',{'formu':formulario,'res':res},RequestContext(request))
def galeria(request):
	return render_to_response('galeria.html',{},RequestContext(request))

def ventas_ent(request):
	
	venta=reservas.objects.all()

	#vent=asientos.objects.filter(idasiento__in=venta)
	return render_to_response("ventas.html",{'venta':venta},context_instance=RequestContext(request))
def res_ent(request):
	
	venta=reservas.objects.all()

	#vent=asientos.objects.filter(idasiento__in=venta)
	return render_to_response("listares.html",{'venta':venta},context_instance=RequestContext(request))
def crear_reporte(request,id):
	hoy = datetime.now().date()
	res=get_object_or_404(reservas,idasiento=id)
	html=render_to_string("factura.html",{'pagesize':'A4','res':res,'hoy':hoy},context_instance=RequestContext(request))
	return generar_pdf(html)
def reportres(request):
	#par=encuentros.objects.all()
	return render_to_response('report.html',{},RequestContext(request))
def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),mimetype='application/pdf')
	return HttpResponse("Error en generar el pdf")
