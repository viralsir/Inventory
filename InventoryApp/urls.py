from django.urls import path, include
from .views import ItemsAV,ItemscategoryAV,ItemsSortAV

urlpatterns = [

    path('items/',ItemsAV.as_view(), name = 'Item-list' ),
    path('items/query/<str:category>/',ItemscategoryAV.as_view(), name = 'Item-Category'),
    path('items/sort/',ItemsSortAV.as_view(), name='Item-Sort')

]
