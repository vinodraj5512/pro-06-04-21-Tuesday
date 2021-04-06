from django.urls import path
from app2  import views

app_name='app2'

urlpatterns = [
    path('<num1>',views.facto,name='map2'),
    path('<num1>/<num2>',views.add,name='map2'),
]
