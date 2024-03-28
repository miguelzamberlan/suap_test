from django.contrib import admin
from django.urls import include, path
# from aluno.views import home
from cidades.alunocid.views import home  # Importado a nova View

# Alterar somente a URL para a nova View

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
