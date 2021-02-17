from django.urls import path
from .views import list_quizview, QuizCreate, QuizDelete, QuizUpdate

urlpatterns = [
    path('list_quiz/', list_quizview, name='list_quiz'),
    path('create_quiz/', QuizCreate.as_view(), name='create_quiz'),
    path('delete_quiz/<int:pk>/', QuizDelete.as_view(), name='delete_quiz'),
    path('update_quiz/<int:pk>/', QuizUpdate.as_view(), name='update_quiz'),

    ]
