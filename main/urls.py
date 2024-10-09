from main import views
from main.views import logout_user
from main.views import login_user
from main.views import register
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import edit_product, delete_product, add_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>/', views.delete_product, name='delete_product'),
    path('', views.home, name='home'),
    path('candle/', views.candle, name='candle'),
    path('light/', views.light, name='light'),
    path('about-us/', views.about_us, name='about_us'),
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
