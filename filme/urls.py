#sempre que for construir uma pagina, preciso desses tres topicos
#1 - Url
#2 - Views
#3 - template

from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilmes, Pesquisafilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_views
app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilmes.as_view(), name='detalhesfilme'),
    path('pesquisa/', Pesquisafilme.as_view(), name='Pesquisafilme'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                              success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]
