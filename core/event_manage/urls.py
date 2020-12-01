

from django.contrib import admin
from django.urls import  path
from django.conf.urls import url
from . import views

urlpatterns = [                          
   path('event/', views.event, name="manage-event"),
   url('^calendareve', views.calendar, name='calendar'),
   url('^add_event$', views.add_event, name='add_event'),
   url('^update$', views.update, name='update'),
   url('^remove', views.remove, name='remove'),
    url('^add_event$', views.add_event, name='add_event_to_end'),

    #path('crud/', views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),

    path('newevent', views.newevent, name='newevent'),

    path('eventreservation/<int:id>', views.update, name='eventreservation'),
]
