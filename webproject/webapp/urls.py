from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.userLogin),
    path('', views.login_page),
    path('homepage', views.homepage, name="homepage"),
    path('signup_page', views.signup_page),
    path('accounts/login/',views.userLogin),
    path('logout',views.logout_view),
    path('productlog/', views.productlog, name='productlog'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('userdata/', views.userdata),
    path('edituser/<int:id>', views.edituser, name="edituser"),
    path('updateuser/<int:user_id>', views.updateuser, name="updateuser"), 
    path('deluser/<int:id>', views.deluser, name="deluser"),     
]


