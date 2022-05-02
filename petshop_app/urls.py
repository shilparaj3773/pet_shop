from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userview/', views.userview, name='userview'),
    path('login/', views.login, name='login'),
    path('admhome/', views.admhome, name='admhome'),
    path('signup1/', views.signup1, name='signup1'),
    path('signup2/', views.signup2, name='signup2'),
    path('cxhome/', views.cxhome, name='cxhome'),
    path('sellerhome/', views.sellerhome, name='sellerhome'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('view_pet/', views.view_pet, name='view_pet'),
    path('payments/<int:id>/', views.payments, name='payments'),
    path('viewpet/', views.viewpet, name='viewpet'),
    path('delete_order/<int:id>', views.delete_order, name='delete_order'),
    path('update_p/<int:id>/', views.update_p, name='update_p'),
    path('delete_pet/<int:id>/', views.delete_pet, name='delete_pet'),
    path('view_order/', views.view_order, name='view_order'),
    path('viewpet_order/', views.viewpet_order, name='viewpet_order'),
    path('add_order/<int:id>/', views.add_order, name='add_order'),
    path('confirm_order/<int:id>/', views.confirm_order, name='confirm_order'),
    path('rej_order/<int:id>/', views.rej_order, name='rej_order'),


]
