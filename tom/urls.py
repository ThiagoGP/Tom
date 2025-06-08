from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from autenticao import views as auth_views

from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.home, name='login'),
    path('callback/', auth_views.amazon_callback, name='amazon_callback'),
    path('home/', dashboard_views.home,  name='dashboard'),
    path('logout/', dashboard_views.logout_view, name='logout'),
    path('registrar-gesto/', dashboard_views.RegistrarGestoView.as_view(), name='registrar_gesto')
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

