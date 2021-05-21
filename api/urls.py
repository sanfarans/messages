from django.urls import path 
from .views import *

urlpatterns = [
    path('', CreateMessage.as_view(), name="create-message"),
    path('<int:message_id>/', ViewMessage.as_view(), name="view-message"),
]