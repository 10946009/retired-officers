from django.urls import path
from admin_panel.views.activity_manage import activity_manage

urlpatterns = [
    path('activity_manage/', activity_manage, name='activity_manage'), 
]