from django.urls import path
from .views import list_historyview, detail_historyview,\
    HistoryCreate, HistoryDelete, HistoryUpdate

urlpatterns = [
    path('list_history/', list_historyview, name='list_history'),
    path('create_history/', HistoryCreate.as_view(), name='create_history'),
    path('detail_history/<int:pk>/', detail_historyview, name='detail_history'),
    path('delete_history/<int:pk>/', HistoryDelete.as_view(), name='delete_history'),
    path('update_history/<int:pk>/', HistoryUpdate.as_view(), name='update_history'),
]
