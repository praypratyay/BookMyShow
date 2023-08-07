from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookTicketView.as_view()),
    path('signup/', views.UserView.as_view())
] 