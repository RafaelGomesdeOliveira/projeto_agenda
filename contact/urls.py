from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [

    path("search/", views.search, name="search"),
    path('', views.index, name='index'),

    #contact (CRUD)
    path("contact/<int:id>/detail/", views.contact, name="contact"),
    path("contact/create/", views.create, name="create"),
    path("contact/<int:id>/update/", views.update, name="update"),
    path("contact/<int:id>/delete/", views.delete, name="delete"),

    #USER (cRUD)
    path("user/create/", views.register, name="register"),
    path("user/login/", views.login_view, name="login"),
    path("user/logout/", views.logout_view, name="logout"),
    path("user/update/", views.user_update, name="user_update"),  

]
