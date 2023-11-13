from django.urls import path

from employees import views

app_name = 'employees'

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('position/', views.position_list, name='position_list'),
    path('position-add/', views.add_position, name='add_position'),
    path('position-edit/<int:id>', views.edit_position, name='edit_position'),
    path('position-delete/<int:id>', views.delete_position, name='delete_position'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>', views.delete_employee, name='delete_employee'),
]
