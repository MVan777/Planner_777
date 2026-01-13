from django import forms
from .models import Tasks
from django.utils import timezone


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'priority', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'Введите название задачи'
            }),
            'description': forms.Textarea(attrs={
                # 'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишите задачу подробно...'
            }),
            'priority': forms.Select(attrs={
                # 'class': 'form-select'
            }),
            'deadline': forms.DateTimeInput(attrs={
                # 'class': 'form-control',
                'type': 'datetime-local'
            })
        }
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'priority': 'Приоритет',
            'deadline': 'Срок выполнения'
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Устанавливаем минимальную дату (сегодня)
        today = timezone.now().strftime('%Y-%m-%dT%H:%M')
        self.fields['deadline'].widget.attrs['min'] = today

    def save(self, commit=True):
        task = super().save(commit=False)
        if self.user:
            task.user = self.user
        if commit:
            task.save()
        return task