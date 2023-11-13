from django import forms

from employees.models import Employee, Position


class EmployeeForm(forms.ModelForm):
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    middle_name = forms.CharField(label='Отчество',
                                  widget=forms.TextInput(attrs={'placeholder': 'Введите отчество'}))
    position = forms.ModelChoiceField(label='Должность', queryset=Position.objects.all())
    invite_date = forms.DateField(label='Дата приема на работу')

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'middle_name', 'position', 'invite_date']


class PositionForm(forms.ModelForm):
    job_title = forms.CharField(label='Должность',
                                widget=forms.TextInput(attrs={'placeholder': 'Введите должность'}))

    class Meta:
        model = Position
        fields = ['job_title']
