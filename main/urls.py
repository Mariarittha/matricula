from django.contrib import admin
from django.urls import path
from aluno.views import aluno_criar,index,aluno_listar,aluno_editar,aluno_remover, curso_listar, curso_criar, curso_editar, curso_remover, cidade_criar, cidade_editar, cidade_listar, cidade_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('aluno/',aluno_criar,name='aluno_criar'),
    path('aluno/editar/<int:id>/',aluno_editar, name='aluno_editar'),
    path('aluno/remover/<int:id>/',aluno_remover,name='aluno_remover'),
    path('aluno/listar',aluno_listar,name='aluno_listar'),
    
    #curso
    path('curso/listar', curso_listar, name='curso_listar'),
    path('curso/criar', curso_criar, name='curso_criar'),
    path('curso/editar/<int:id>/',curso_editar,name='curso_editar'),
    path('curso/remover/<int:id>/',curso_remover,name='curso_remover'),
    
    #cidade
    path('cidade/',cidade_criar,name='cidade_criar'),
    path('cidade/editar/<int:id>/',cidade_editar, name='cidade_editar'),
    path('cidade/remover/<int:id>/',cidade_remover,name='cidade_remover'),
    path('cidade/listar',cidade_listar,name='cidade_listar'),
]



