from django.urls import path
from firstapp import views

urlpatterns = [
    path('a1/',views.add_show,name='add'),
    path('a2/<int:id>/',views.delete_data,name='deletedata'),
    path('a3/<int:id>/',views.update_data,name='updatedata'),
]

