# Generated by Django 4.1 on 2023-08-22 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foreman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('position', models.CharField(max_length=200, verbose_name='должность')),
                ('entry_date', models.DateField(verbose_name='дата приема на работу')),
                ('salary', models.IntegerField(verbose_name='зарплата')),
            ],
            options={
                'verbose_name': 'бригадир',
                'verbose_name_plural': 'бригадиры',
                'db_table': 'foreman',
            },
        ),
        migrations.CreateModel(
            name='GeneralManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('position', models.CharField(max_length=200, verbose_name='должность')),
                ('entry_date', models.DateField(verbose_name='дата приема на работу')),
                ('salary', models.IntegerField(verbose_name='зарплата')),
            ],
            options={
                'verbose_name': 'ген.директор',
                'verbose_name_plural': 'ген.директора',
                'db_table': 'generalmanager',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('position', models.CharField(max_length=200, verbose_name='должность')),
                ('entry_date', models.DateField(verbose_name='дата приема на работу')),
                ('salary', models.IntegerField(verbose_name='зарплата')),
                ('boss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='app.foreman', verbose_name='кто начальник')),
            ],
            options={
                'verbose_name': 'рабочий',
                'verbose_name_plural': 'рабочие',
                'db_table': 'worker',
            },
        ),
        migrations.CreateModel(
            name='TopManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('position', models.CharField(max_length=200, verbose_name='должность')),
                ('entry_date', models.DateField(verbose_name='дата приема на работу')),
                ('salary', models.IntegerField(verbose_name='зарплата')),
                ('boss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='app.generalmanager', verbose_name='кто начальник')),
            ],
            options={
                'verbose_name': 'топ.менеджер',
                'verbose_name_plural': 'топ.менеджеры',
                'db_table': 'topmanager',
            },
        ),
        migrations.CreateModel(
            name='MiddleManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('position', models.CharField(max_length=200, verbose_name='должность')),
                ('entry_date', models.DateField(verbose_name='дата приема на работу')),
                ('salary', models.IntegerField(verbose_name='зарплата')),
                ('boss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='app.topmanager', verbose_name='кто начальник')),
            ],
            options={
                'verbose_name': 'мидл.менеджер',
                'verbose_name_plural': 'мидл.менеджеры',
                'db_table': 'middlemanager',
            },
        ),
        migrations.AddField(
            model_name='foreman',
            name='boss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='app.middlemanager', verbose_name='кто начальник'),
        ),
    ]