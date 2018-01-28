from django.urls import path
from . import views

app_name = 'charitown'
urlpatterns = [
    # ex: /charitown/
    path('', views.index, name='default'),
    # ex: /charitown/
    path('index.html', views.index, name='index'),
    # ex: /charitown/view_profile.html
    path('view_profile.html', views.profile, name='profile'),
    # ex: /charitown/create_account.html
    path('create_account.html', views.create, name='create'),
    # ex: /charitown/about.html
    path('about.html', views.about, name='about'),
    # ex: /charitown/modify_community.html
    path('modify_community.html', views.mod_community, name='mod_community'),
    # ex: /charitown/modify_user.html
    path('modify_user.html', views.mod_user, name='mod_user'),
    # ex: /charitown/view_city.html
    path('view_city.html', views.city, name='city'),
    # ex: /charitown/search_results.html
    path('search_results.html', views.search, name='search'),
    # ex: /charitown/login.html
    path('login.html', views.login_page, name='login'),
]
