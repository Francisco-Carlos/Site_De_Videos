from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from Midias import settings

urlpatterns =[
    #padrao index,detalhes,cadastrar.
    path('',views.Index,name='index'),
    path('',views.Creat_Coment),
    path('heart/usuario/',views.Usuario),
    path('heart/detalhe/<int:id>',views.Detalhes),
    path('heart/cadastrar/',views.Cadastrar),
    #usuarios cadastrados
    path('heart/Cadastrar_user/',views.Cadastrar_User),
    #cadastrar perfil
    path('heart/Cadastrar_perfil/',views.Cadastar_perfil),
    # login e logouf
    path('heart/login/',views.Login),
    path('heart/login/submit',views.Login_user),
    path('heart/logout/',views.Logout),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)