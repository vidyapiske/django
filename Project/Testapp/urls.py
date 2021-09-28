from django.urls import path
from . import views
app_name="Testapp"
urlpatterns=[
    path('new1',views.Hii),
    path('new2',views.Hello),
]