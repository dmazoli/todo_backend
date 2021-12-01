# Generated by Django 3.2.9 on 2021-12-01 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='01-12-2021')),
                ('due_date', models.DateField(default='01-12-2021')),
                ('completed', models.BooleanField()),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todo_api.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
