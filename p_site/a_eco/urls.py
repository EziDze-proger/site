
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ecohome.as_view(), name='home'),
    path("search/", search.as_view(), name="search"),
    path("about/", plug.as_view(), name="about us"),
    path("contacts/", contacts_plug.as_view(), name="contacts"),
    path("product/<slug:slug>/", product.as_view(), name="post_product"),
    path("support/", technical_support.as_view(), name="support_for_user"),
    path("register/", register_user.as_view(), name="register"),
    path("login/", login_user.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("link/", link.as_view(), name="link"),
]

# {% if request.user.is_authenticated %}<a href="#" class="user-log-in">{{user.username}}<div>выйти</div></a>{% else %}
# <a href="{% url 'login' %}" class="header-login"><div>Авторизация</div></a><a href="{% url 'register' %}" class="header-sign-up"><div>Регистрация</div></a>

