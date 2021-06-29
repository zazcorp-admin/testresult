from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('login', views.loginFunc, name='Login'),
    path('logout', views.logoutFunc, name='Logout'),
    path('admin_panel', views.adminPanel, name='AdminPanel'),
    path('add_test', views.AddTestView.as_view(), name='AddTest'),
    path('terms', views.terms_and_condition, name='Terms'),
    path('<int:pk>', views.desc, name='Desc'),
    path('delete_test/<int:pk>', views.delete_test, name='DeleteOrder'),
    path('update_test/<int:pk>', views.updateTest, name='UpdateOrder'),
    path('update_terms/<int:pk>', views.update_terms, name='UpdateTerms')

]