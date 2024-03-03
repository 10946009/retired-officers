from django.urls import path
from admin_panel.views.activity_manage import activity_manage
from admin_panel.views.activity_create import activity_create
from admin_panel.views.activity_update import activity_update
from admin_panel.views.activity_delete import activity_delete

urlpatterns = [
    path('activity_manage/', activity_manage, name='activity_manage'), 
    path('activity_create/', activity_create, name='activity_create'), 
    path('activity_update/<int:activity_id>', activity_update, name='activity_update'), 
    path('activity_delete/<int:activity_id>', activity_delete, name='activity_delete'), 
]