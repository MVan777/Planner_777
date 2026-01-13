from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    ORDINARY = 'ordinary'
    AVERAGE = 'average'
    URGENT = 'urgent'

    PRIORITY_CHOICES = [
        (ORDINARY, 'Обычный'),
        (AVERAGE, 'Средний'),
        (URGENT, 'Срочный'),
    ]

    title = models.CharField(max_length=50, verbose_name='Название задачи')
    description = models.TextField(max_length=500, verbose_name='Описание задачи')
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default=ORDINARY,verbose_name='Приоритет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks',verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']
