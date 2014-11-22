from django.shortcuts import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import ContactoForm, RecetaForm, ComentarioForm
from principal.models import Receta, Comentario

def sobre(request):
	usuario = request.user	
	return render_to_response('Acercade.html',{'usuario':usuario }, context_instance=RequestContext(request))

def inicio(request):
	recetas = Receta.objects.all()
	usuario = request.user	
	return render_to_response('inicio.html',{'recetas':recetas,'usuario':usuario}, context_instance=RequestContext(request))
		
"""def usuarios(request):
	usuario = User.objects.all()
	recetas = Receta.objects.all()
	return render_to_response('usuarios.html',{'usuario':usuario,'recetas':recetas},context_instance=RequestContext(request))
	"""
	
def lista_recetas(request):
	usuario = request.user
	recetas = Receta.objects.all()
	return render_to_response('recetas.html',{'datos':recetas, 'usuario':usuario}, context_instance=RequestContext(request))
		
def detalle_receta(request,id_receta):
	dato = get_object_or_404(Receta, pk=id_receta)
	usuario = request.user	
	comentarios = Comentario.objects.filter(receta=dato)
	return render_to_response('receta.html',{'receta':dato,'comentario':comentarios,'usuario':usuario}, context_instance=RequestContext(request))
	
	
def contacto(request):
	usuario = request.user	
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde el recetario'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a:' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['luis.ovidio.gonzalez@correounivalle.edu.co'])
			correo.send()
			return HttpResponseRedirect('/')
	else :
		formulario = ContactoForm()
	return render_to_response('contacto.html',{'formulario': formulario,'usuario':usuario},context_instance=RequestContext(request))
	
@login_required(login_url='/ingresar')
def nueva_receta(request):
	usuario = request.user	
	if request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = RecetaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/recetas')
	else:
		formulario = RecetaForm()
	return render_to_response('recetaform.html',{'formulario':formulario,'usuario':usuario},context_instance=RequestContext(request))
		
				
def nuevo_comentario(request):
	usuario = request.user	
	if request.method =='POST':
		formulario = ComentarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/receta')
 	else:
 		formulario = ComentarioForm()
 	return render_to_response('comentarioform.html',{'formulario':formulario,'usuario':usuario},context_instance=RequestContext(request))
 	
	
def nuevo_usuario(request):
	usuario = request.user
	
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
			
	else:
		formulario = UserCreationForm()
	return render_to_response ('nuevousuario.html',{'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))
	
	
def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']		
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html',context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))
	
	
@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	return render_to_response('privado.html',{'usuario':usuario}, context_instance=RequestContext(request))
	
@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')