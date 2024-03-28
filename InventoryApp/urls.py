from django.urls import path, include
from .views import ItemsAV

urlpatterns = [

    path('items/',ItemsAV.as_view(), name = 'Item-list' ),
    

]
