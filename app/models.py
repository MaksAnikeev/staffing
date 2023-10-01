from django.db import models


class Employee(models.Model):
    fullname = models.CharField(
        max_length=200,
        verbose_name='ФИО'
    )
    position = models.CharField(
        max_length=200,
        verbose_name='должность'
    )
    entry_date = models.DateField(
        verbose_name='дата приема на работу'
    )
    salary = models.IntegerField(
        verbose_name='зарплата'
    )
    boss = models.ForeignKey(
        'self',
        related_name='subordinates',
        verbose_name='кто начальник',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'employee'
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self):
        return self.fullname