from django.urls import path
from cut_app import views


app_name = 'cut_app'

urlpatterns = [
    path('', views.Index_View.as_view(), name='index'),
    path('<str:short_url>', views.Redirect_me_View.as_view(), name='short'),
]