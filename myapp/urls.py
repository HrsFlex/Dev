from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact_us'),
    path('about/',views.about,name='about_us'),
    path('service/',views.service,name='service'),
    path('detail/',views.detail,name='detail'),
    path('prediction/',views.prediction,name='prediction'),
    path('realiablity/',views.proof,name='proof'),
    path('ai-input/', views.ai_response_view, name='ai_input'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('subscribe/',views.subscribe,name='subscribe'),
]
