
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "GasyKaly",
        default_version = "1.0.0",
        description = "Recette pour les plats Malagasy"
        ),
    public = True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include([
        path('kaly/', include('Recipe.urls'), name='recipe'),
        path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger_schema"),
        ]) 
        )]
