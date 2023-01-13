from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
  path('',views.index,name='index'),
  path('search/',views.search,name='search'),
  path('adminpage/',views.adminpage,name='adminpage'),
  path('login/',views.signin,name='signin'),
  path('logout/',views.logot,name='logout'),
  path('signup/',views.signup,name='signup'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('Ad/', views.Ad, name='Ad'),
  path('find/', views.find, name='find'),

  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)