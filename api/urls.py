from django.urls import path 
from .views import *

urlpatterns = [
    path('', CreateMessage.as_view()),
    path('<int:message_id>/', ViewMessage.as_view()),
]