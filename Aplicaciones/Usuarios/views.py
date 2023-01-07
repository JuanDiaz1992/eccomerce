from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from Aplicaciones.tiendaEnLinea.forms import FormularioLogin,UserRegisterForm,editarDatos
from django.http import HttpResponseRedirect
from .models import User, PerfilUsuario
from django.contrib import messages
from django.shortcuts import render,redirect



class Login (FormView):
    template_name = 'registration/login.html'

    form_class = FormularioLogin

    success_url = reverse_lazy('tiendaEnLinea:index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args, **kwargs)

    def form_valid(self, form):
        login(self.request,form.get_user())
        return super (Login,self).form_valid(form)

def LogoutUsuario(request):
    logout(request)
    messages.success(request,"Te has deslogueado del sistema")
    return redirect("tiendaEnLinea:index")



def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        success = False
        if form.is_valid():
            datos = form.save(commit=False)
            datos.save()
            user = form.cleaned_data['username']
            user = User.objects.get(username = user)
            userID = user.id
            primerNombre = form.cleaned_data['nombre1']
            segundoNombre = form.cleaned_data['nombre2']
            primerApellido = form.cleaned_data['primerApellido']
            segundoApellido = form.cleaned_data['segundoApellido']
            us = PerfilUsuario.objects.get(user_id = userID )
            us.nombre1 = primerNombre
            us.nombre2 = segundoNombre
            us.primerApellido = primerApellido
            us.segundoApellido = segundoApellido
            us.save()
            usename = form.cleaned_data ['username']
            success = True
            messages.add_message(request, messages.INFO, f'Usuario {usename} registrado correctamente, ahora disfruta de todo el contenido que tenemos para ti.')
            return render(request, 'registration/creado.html', {'form': form})
        else:
            messages.success(request, f' Datos incorrectos, vuelve a intentarlo')
            

    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render (request, "registration/registrer.html", context)



def modificarPerUsuario(request):
    user = request.user.id
    us = PerfilUsuario.objects.get(user_id = user)  

    if request.method == 'POST':
        form = editarDatos(request.POST, request.FILES, instance= us)
        if form.is_valid():            
            nom1 = request.POST.get('nombre1')            
            nom2 = request.POST.get('nombre2')            
            apel1 = request.POST.get('primerApellido')            
            apel2 = request.POST.get('segundoApellido')
            dir = request.POST.get('direccion')
            depart = request.POST.get('departamento')
            ciudad = request.POST.get('ciudad')
            cel = request.POST.get('celular')
            us.nombre1 = nom1
            us.nombre2 = nom2
            us.segundoApellido = apel2
            us.primerApellido = apel1
            us.departamento = depart
            us.ciudad = ciudad
            us.direccion = dir
            us.celular = cel

            us.save()
            return redirect ('/')
    else:
        form=editarDatos(instance=us)
    context={
            'form':form,
        }
    return render (request, "registration/edicionPerfilUs.html", context)