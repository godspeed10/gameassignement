from django.urls import path
from .views import *


urlpatterns = [
    path('StartGame', StartGame.as_view()),
    path('UpdateBoard', UpdateBoard.as_view()),
    path('GameAPI', ListofGamedata.as_view()),


]
