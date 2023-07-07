
from django.urls import path
from .views import ToyListView, ToyDetailView, GiftCreateView

urlpatterns = [
    path('', ToyListView.as_view(), name='toy_list'),
    path('<int:pk>/', ToyDetailView.as_view(), name='toy_detail'),
    path('gifts/create/', GiftCreateView.as_view(), name='gift_create'),

]
