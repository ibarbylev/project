from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^csv', views.download_csv_for_exercise, name='download_csv_for_exercise'),

]

