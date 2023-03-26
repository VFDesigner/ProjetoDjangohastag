from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarcontaForm, FormHome
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#def homepage(request):
#    return render(request, "Homepage.html")

class Homepage(FormView):
    template_name = "Homepage.html"
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

#def homefilmes(request):
 #   context = {}
  #  lista_filmes = Filme.objects.all()
   # context['lista_filmes'] = lista_filmes
    #return render(request, "homefilmes.html", context)

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object List -> Lista de itens do modelo

class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    #object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        #descobrir qual filme ele esta acessando
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        #somar 1 na view daquele filme
        #sempre salvar
        usuario = request.user
        usuario.filme_vistos.add(filme)
        return super().get(request, *args, **kwargs) #isso redireciona o usuario para a url final


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        #Quero filtrar o filmes pegando por categorias
        self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context

class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme
    #object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarcontaForm
    #form valid valida as informações passada pelo usuario na hora de criar a conta
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
