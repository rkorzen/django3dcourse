from django.urls import path
from .views import do_math


urlpatterns = [
    path("<op>/<int:a>/<int:b>/", do_math),

]