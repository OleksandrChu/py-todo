# Generated by Django 3.1.3 on 2020-11-02 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.todolist')),
            ],
        ),
    ]
