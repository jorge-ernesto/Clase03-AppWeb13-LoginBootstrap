from django.urls import path
from . import views
urlpatterns = [
    path('',views.render_login,name='render_login'),

]
