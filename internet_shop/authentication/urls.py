from django.urls import path, include

from .views import RegisterView, LoginView, LogoutView, UserPasswordUpdateView, UsersViewWithParam, \
    UsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('users/', UsersView.as_view(), name="users"),
    path('users/<int:id>/', UsersViewWithParam.as_view(), name="users_retrieve"),
    path('change_password/<int:id>/', UserPasswordUpdateView.as_view(), name="change_password"),
]