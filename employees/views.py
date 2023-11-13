from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView

from common.views import TitleMixin
from employees.forms import EmployeeForm, PositionForm
from employees.models import Employee, Position


class IndexView(TitleMixin, TemplateView):
    template_name = 'site/index.html'
    title = 'Store'


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees:employee_list'))
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})


def edit_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees:employee_list'))
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        employee.delete()
        return HttpResponseRedirect(reverse('employees:employee_list'))
    return render(request, 'employees/confirm_delete.html', {'employee': employee})


def position_list(request):
    position = Position.objects.all()
    return render(request, 'position/position_list.html', {'positions': position})


def edit_position(request, id):
    position = get_object_or_404(Position, pk=id, )
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees:position_list'))
    else:
        form = PositionForm(instance=position)
    return render(request, 'position/edit_position.html', {'form': form})


def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees:position_list'))
    else:
        form = PositionForm()
    return render(request, 'position/add_position.html', {'form': form})


def delete_position(request, id):
    position = get_object_or_404(Position, pk=id)
    if request.method == 'POST':
        position.delete()
        return HttpResponseRedirect(reverse('employees:position_list'))
    return render(request, 'position/confirm_delete.html', {'position': position})
