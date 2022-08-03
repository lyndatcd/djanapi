from django.urls import path
from . import views

app_name="link"

urlpatterns = [
    path("active/", views.ActiveLinkView.as_view(), name='active_link'),
    path("recent/", views.RecentLinkView.as_view(), name='recent_link'),
]