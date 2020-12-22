from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', Quiz.as_view() , name="quiz"),
    path('r/<str:topic>/', RandomQuestion.as_view() , name ="random"),
    path('q/<str:topic>/', QuizQuestion.as_view() , name ="questions"),
]
