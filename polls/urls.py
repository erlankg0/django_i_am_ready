from django.urls import path
from .views import IndexView, vote, DetailViews, ResultViews

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailViews.as_view(), name='detail'),
    path('<int:pk>/results/', ResultViews.as_view(), name='results'),
    path('<int:pk>/votes/', vote, name='vote'),
]
