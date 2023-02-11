from django.urls import path
from .views import *

urlpatterns = [
  path('PlayerRegister', PlayerRegister.as_view()),
  # path('getrole', Role.as_view()),

  # path('customerregister', EmployeeRegisterView.as_view()),
  # path('me', RetrieveUserView.as_view()),
]