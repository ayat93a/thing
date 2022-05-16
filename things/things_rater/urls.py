from unicodedata import name
from django.urls import path
from .views import ThingListView , ThingDetailView ,HomeView , ThingCreateView , ThingUpdateView , ThingDeleteView

urlpatterns = [
    path('things-list' , ThingListView.as_view() , name= 'things_list'),
    path('<int:pk>' , ThingDetailView.as_view() , name = 'things_detail' ),
    path('' , HomeView.as_view(), name= 'home_view' ),
    path('create/' , ThingCreateView.as_view() , name = 'create_thing' ),
    path('update/<int:pk>' , ThingUpdateView.as_view() , name = 'update_thing'),
    path('delete/<int:pk>' , ThingDeleteView.as_view() , name= 'delete')
]
