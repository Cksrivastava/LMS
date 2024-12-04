from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='library-dashboard'),  # Set the root of the library app to the dashboard view
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_member/', views.add_member, name='add_member'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('pay_fine/', views.pay_fine, name='pay_fine'),
    path('update_membership/', views.update_membership, name='update_membership'),
    path('user_management/', views.user_management, name='user_management'),
]